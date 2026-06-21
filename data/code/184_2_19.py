import json

class JsonKeywordSearcher:

    def __init__(self):
        self.target_keyword = None
        self.found_paths = []

    def search(self, data, current_path=''):
        if isinstance(data, dict):
            for key, value in data.items():
                new_path = f'{current_path}.{key}' if current_path else key
                self.search(value, new_path)
        elif isinstance(data, list):
            for index, item in enumerate(data):
                new_path = f'{current_path}[{index}]'
                self.search(item, new_path)
        elif data == self.target_keyword:
            self.found_paths.append(current_path)

    def find_keyword(self, json_payload, target_keyword):
        self.target_keyword = target_keyword
        self.found_paths = []
        self.search(json_payload)
        return self.found_paths
if __name__ == '__main__':
    searcher = JsonKeywordSearcher()
    sample_json_payload = {'root': {'level1': [{'key1': 'value1'}, {'key2': 'target_keyword'}], 'level2': {'key3': ['target_keyword', 'value4']}}}
    target_word = 'target_keyword'
    result = searcher.find_keyword(sample_json_payload, target_word)
    print(result)