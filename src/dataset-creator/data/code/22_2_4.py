class KeyMatcher:
    def compare_and_intersect(self, dict1: dict, dict2: dict) -> set:
        set1 = set(dict1.keys())
        set2 = set(dict2.keys())
        return set1.intersection(set2)
if __name__ == '__main__':
    matcher = KeyMatcher()
    data1 = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5
    }
    data2 = {
        'c': 9,
        'd': 8,
        'e': 7,
        'f': 10,
        'g': 11
    }
    intersection_keys = matcher.compare_and_intersect(data1, data2)
    print(f"Dictionary 1: {data1}")
    print(f"Dictionary 2: {data2}")
    print(f"Intersection of keys: {intersection_keys}")