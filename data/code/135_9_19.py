import xml.etree.ElementTree as ET

def strip_namespaces_and_attributes(xml_str):

    def strip_ns_and_attrs(elem):
        tag = elem.tag.split('}')[1] if '}' in elem.tag else elem.tag
        new_elem = ET.Element(tag)
        for child in elem:
            new_child = strip_ns_and_attrs(child)
            new_elem.append(new_child)
        return new_elem
    root = ET.fromstring(xml_str)
    stripped_root = strip_ns_and_attrs(root)
    return ET.tostring(stripped_root, encoding='unicode')

def sort_children(elem):
    for child in elem:
        sort_children(child)
    elem[:] = sorted(elem, key=lambda x: x.tag)

def compare_xmls(xml1, xml2):
    stripped_xml1 = strip_namespaces_and_attributes(xml1)
    stripped_xml2 = strip_namespaces_and_attributes(xml2)
    root1 = ET.fromstring(stripped_xml1)
    root2 = ET.fromstring(stripped_xml2)
    sort_children(root1)
    sort_children(root2)
    return stripped_xml1 == stripped_xml2
if __name__ == '__main__':
    xml1 = '\n    <root xmlns="ns1">\n        <child attr="a">text1</child>\n        <child attr="b">text2</child>\n    </root>\n    '
    xml2 = '\n    <root>\n        <child>text1</child>\n        <child>text2</child>\n    </root>\n    '
    result = compare_xmls(xml1, xml2)
    print(result)