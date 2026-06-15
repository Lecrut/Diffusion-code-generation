class KeyMatcher:
    def find_intersection(self, dict1: dict, dict2: dict) -> set:
        set1 = set(dict1.keys())
        set2 = set(dict2.keys())
        return set1.intersection(set2)
if __name__ == '__main__':
    data1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    data2 = {'c': 5, 'd': 6, 'e': 7, 'f': 8}
    matcher = KeyMatcher()
    intersection_keys = matcher.find_intersection(data1, data2)
    print(intersection_keys)