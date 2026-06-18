class KeyMatcher:
    def match(self, dict1, dict2):
        if not dict1 or not dict2:
            return {}
        result = {}
        for key, value1 in dict1.items():
            if key in dict2:
                value2 = dict2[key]
                if value1 == value2:
                    result[key] = value1
        return result
if __name__ == '__main__':
    matcher = KeyMatcher()
    data1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    data2 = {'a': 1, 'b': 99, 'c': 3, 'e': 5}
    matched_data = matcher.match(data1, data2)
    print(matched_data)