class KeyMatcher:
    def compare_and_intersect(self, dict1: dict, dict2: dict) -> set:
        set1 = set(dict1.keys())
        set2 = set(dict2.keys())
        return set1.intersection(set2)
if __name__ == '__main__':
    matcher = KeyMatcher()
    dict_a = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    dict_b = {'c': 9, 'd': 8, 'e': 5, 'f': 6}
    intersection = matcher.compare_and_intersect(dict_a, dict_b)
    print(intersection)