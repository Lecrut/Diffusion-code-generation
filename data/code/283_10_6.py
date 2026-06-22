class UniqueElementsChecker:
    @staticmethod
    def are_elements_unique(lst):
        seen = set()
        for item in lst:
            if not isinstance(item, (int, str)):
                raise ValueError("List contains non-hashable elements")
            if item in seen:
                return False
            seen.add(item)
        return True

if __name__ == '__main__':
    checker = UniqueElementsChecker()
    sample_list = [1, 2, 3, 4, 5]
    print(checker.are_elements_unique(sample_list))
    sample_list_with_non_hashable = [1, 2, 'a', {'b': 2}, 5]
    try:
        print(checker.are_elements_unique(sample_list_with_non_hashable))
    except ValueError as e:
        print(f"Error: {e}")