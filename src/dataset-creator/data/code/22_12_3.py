class KeyMatcher:
    def match(self, dict1: dict, dict2: dict) -> bool:
        if len(dict1) != len(dict2):
            return False
        for key, value1 in dict1.items():
            if key not in dict2:
                return False
            if dict2[key] != value1:
                return False
        return True
if __name__ == '__main__':
    matcher = KeyMatcher()
    dict_a = {'a': 1, 'b': 2, 'c': 3}
    dict_b = {'a': 1, 'b': 2, 'c': 3}
    dict_c = {'a': 1, 'b': 99, 'c': 3}
    dict_d = {'a': 1, 'b': 2}
    print(f"Match A and B: {matcher.match(dict_a, dict_b)}")
    print(f"Match A and C: {matcher.match(dict_a, dict_c)}")
    print(f"Match A and D: {matcher.match(dict_a, dict_d)}")
    print(f"Match B and A: {matcher.match(dict_b, dict_a)}")
    print(f"Match C and B: {matcher.match(dict_c, dict_b)}")