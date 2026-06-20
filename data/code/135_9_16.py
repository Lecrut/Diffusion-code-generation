import xml.etree.ElementTree as ET

def strip_namespaces_and_attributes(element):
    for elem in element.iter():
        if '}' in elem.tag:
            elem.tag = elem.tag.split('}', 1)[1]
        del elem.attrib
    return element

def sort_child_elements(element):
    for child in element:
        child[:] = sorted(child, key=lambda x: (x.tag, x.text))
    return element

def compare_xml_documents(xml1, xml2):
    tree1 = ET.fromstring(xml1)
    tree2 = ET.fromstring(xml2)

    stripped_tree1 = strip_namespaces_and_attributes(tree1)
    stripped_tree2 = strip_namespaces_and_attributes(tree2)

    sorted_tree1 = sort_child_elements(stripped_tree1)
    sorted_tree2 = sort_child_elements(stripped_tree2)

    return ET.tostring(sorted_tree1) == ET.tostring(sorted_tree2)

if __name__ == '__main__':
    xml1 = '<root><child>value</child></root>'
    xml2 = '<root><child>value</child></root>'
    print(compare_xml_documents(xml1, xml2))