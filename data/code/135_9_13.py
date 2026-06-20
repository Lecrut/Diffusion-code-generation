import xml.etree.ElementTree as ET

def normalize_xml_element(element):
    element.tag = element.tag.split('}')[-1] if '}' in element.tag else element.tag
    for attr in list(element.attrib.keys()):
        del element.attrib[attr]
    for child in element:
        normalize_xml_element(child)
    return sorted(element.getchildren(), key=lambda x: (x.tag, str(x.text)))

def normalize_xml(xml_str):
    root = ET.fromstring(xml_str)
    return ''.join(ET.tostring(normalize_xml_element(root), 'unicode'))

def check_equivalence(xml1, xml2):
    return normalize_xml(xml1) == normalize_xml(xml2)

if __name__ == '__main__':
    xml1 = '<root xmlns="ns"><child>text</child></root>'
    xml2 = '<root><child>text</child></root>'
    print(check_equivalence(xml1, xml2))