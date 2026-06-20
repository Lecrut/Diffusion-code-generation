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
    root1 = ET.fromstring(xml1)
    root2 = ET.fromstring(xml2)

    strip_namespaces_and_attributes(root1)
    strip_namespaces_and_attributes(root2)

    sort_child_elements(root1)
    sort_child_elements(root2)

    return ET.tostring(root1) == ET.tostring(root2)

if __name__ == '__main__':
    xml1 = '<root><child>text</child></root>'
    xml2 = '<root><child>text</child></root>'
    print(compare_xml_documents(xml1, xml2))