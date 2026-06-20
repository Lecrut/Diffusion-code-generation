import xml.etree.ElementTree as ET

def strip_namespaces_and_attributes(element):
    for elem in element.iter():
        if '}' in elem.tag:
            elem.tag = elem.tag.split('}')[1]
        del elem.attrib
    return element

def sort_child_elements(element):
    for child in element:
        sort_child_elements(child)
    element[:] = sorted(element, key=lambda x: (x.tag, x.text))

def compare_xml_documents(xml1, xml2):
    tree1 = ET.fromstring(xml1)
    tree2 = ET.fromstring(xml2)

    strip_namespaces_and_attributes(tree1)
    strip_namespaces_and_attributes(tree2)

    sort_child_elements(tree1)
    sort_child_elements(tree2)

    return ET.tostring(tree1) == ET.tostring(tree2)

if __name__ == '__main__':
    xml1 = '<root><child>text</child></root>'
    xml2 = '<root><child>text</child></root>'
    print(compare_xml_documents(xml1, xml2))