import json

def find_keyword_in_json(payload, target_keyword):

    def search_element(element):
        if isinstance(element, dict):
            return any((search_element(value) for value in element.values()))
        elif isinstance(element, list):
            return any((search_element(item) for item in element))
        elif isinstance(element, str) and target_keyword in element:
            return True
        return False
    return search_element(payload)
if __name__ == '__main__':
    sample_json = '\n    {\n        "root": {\n            "middle": {\n                "leaf1": "The quick brown fox",\n                "leaf2": ["jumps", "over", "the", "lazy dog"]\n            },\n            "another_leaf": "Another line with the fox"\n        }\n    }\n    '
    sample_payload = json.loads(sample_json)
    target_word = 'fox'
    result = find_keyword_in_json(sample_payload, target_word)
    print(result)