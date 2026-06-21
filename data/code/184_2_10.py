import json

class JsonKeywordSearcher:
    TARGET_KEYWORD = 'target'
    
    @staticmethod
    def search_key_in_json(json_data, target_keyword=TARGET_KEYWORD):
        if isinstance(json_data, dict):
            return any(JsonKeywordSearcher.search_key_in_json(value, target_keyword) for value in json_data.values())
        elif isinstance(json_data, list):
            return any(JsonKeywordSearcher.search_key_in_json(item, target_keyword) for item in json_data)
        elif isinstance(json_data, str):
            return target_keyword in json_data
        return False

if __name__ == '__main__':
    sample_json = {
        "key1": "value1",
        "key2": {
            "subkey1": "target value",
            "subkey2": [
                "another value",
                {"nested_key": "target"}
            ]
        },
        "key3": "value3"
    }
    
    searcher = JsonKeywordSearcher()
    result = searcher.search_key_in_json(sample_json)
    print(result)