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

def are_xmls_semantically_equivalent(xml1, xml2):
    root1 = ET.fromstring(xml1)
    root2 = ET.fromstring(xml2)

    strip_namespaces_and_attributes(root1)
    strip_namespaces_and_attributes(root2)

    sort_child_elements(root1)
    sort_child_elements(root2)

    return xml_to_text(root1) == xml_to_text(root2)

if __name__ == '__main__':
    sample_xml1 = """
    <root xmlns="http://example.com">
        <child attr="value">text</child>
    </root>
    """

    sample_xml2 = """
    <root>
        <child>text</child>
    </root>
    """

    print(are_xmls_semantically_equivalent(sample_xml1, sample_xml2))