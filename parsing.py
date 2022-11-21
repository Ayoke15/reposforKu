import xml.dom.minidom


def main():

    doc = xml.dom.minidom.parse("postamats.xml");
    print(doc.nodeName)
    print(doc.firstChild.tagName)
    f = open('postamats.txt', 'w')
    i = 1
    pt = doc.getElementsByTagName("pt")
    for p in pt:
        if p.getElementsByTagName("City")[0].firstChild.nodeValue == "Москва":
            first = p.getElementsByTagName("latitude")[0].firstChild.data
            second = p.getElementsByTagName("longitude")[0].firstChild.data
            newFirst = first.replace(',', '.')
            newSecond = second.replace(',', '.')
            nums= [newFirst,newSecond]
            f.write("({}, {}) \n".format(*nums))
    f.close();
if __name__ == "__main__":
    main();
