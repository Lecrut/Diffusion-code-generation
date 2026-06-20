import xml.etree.ElementTree as ET

def strip_namespaces_and_attributes(element):
    for elem in element.iter():
        if '}' in elem.tag:
            elem.tag = elem.tag.split('}')[1]
        elem.attrib.clear()
    return element

def sort_child_elements(element):
    for child in element:
        sort_child_elements(child)
    element[:] = sorted(element, key=lambda x: (x.tag, x.text))

def xml_to_text(element):
    return ET.tostring(element, encoding='unicode')

def are_xml_documents_equivalent(xml1, xml2):
    tree1 = ET.fromstring(xml1)
    tree2 = ET.fromstring(xml2)

    stripped_tree1 = strip_namespaces_and_attributes(tree1)
    stripped_tree2 = strip_namespaces_and_attributes(tree2)

    sorted_tree1 = sort_child_elements(stripped_tree1)
    sorted_tree2 = sort_child_elements(stripped_tree2)

    text1 = xml_to_text(sorted_tree1)
    text2 = xml_to_text(sorted_tree2)

    return text1 == text2

if __name__ == '__main__':
    xml1 = '<root><child>text</child></root>'
    xml2 = '<root><child>text</child></root>'
    print(are_xml_documents_equivalent(xml1, xml2))