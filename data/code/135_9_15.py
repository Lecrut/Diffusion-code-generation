import xml.etree.ElementTree as ET

def strip_ns_and_attrs(elem):
    if elem.tag.startswith('{'):
        elem.tag = elem.tag.split('}')[1]
    for child in elem:
        strip_ns_and_attrs(child)
    del elem.attrib

def sort_child_elements(elem):
    sorted_children = sorted(elem, key=lambda child: child.tag)
    for i, child in enumerate(sorted_children):
        elem[i] = child
        sort_child_elements(child)

def to_text_representation(elem):
    return ET.tostring(elem, encoding='unicode')

def check_equivalence(xml1, xml2):
    root1 = ET.fromstring(xml1)
    root2 = ET.fromstring(xml2)
    strip_ns_and_attrs(root1)
    sort_child_elements(root1)
    strip_ns_and_attrs(root2)
    sort_child_elements(root2)
    return to_text_representation(root1) == to_text_representation(root2)
if __name__ == '__main__':
    xml1 = '\n    <root>\n        <b>2</b>\n        <a>1</a>\n    </root>\n    '
    xml2 = '\n    <root>\n        <a>1</a>\n        <b>2</b>\n    </root>\n    '
    print(check_equivalence(xml1, xml2))