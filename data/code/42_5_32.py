class StringManipulator:
    def merge_fragments(self, fragments: list[str]) -> str:
        if not self._is_valid_input(fragments):
            return ""
        return "".join(fragments)

    def _is_valid_input(self, fragments: list[str]) -> bool:
        return isinstance(fragments, list) and all(isinstance(fragment, str) for fragment in fragments)

if __name__ == '__main__':
    manipulator = StringManipulator()
    test_case_1 = ["Hello", " ", "World"]
    result_1 = manipulator.merge_fragments(test_case_1)
    print(f"Test Case 1: '{result_1}'")
    
    test_case_2 = ["Python", "is", "fun"]
    result_2 = manipulator.merge_fragments(test_case_2)
    print(f"Test Case 2: '{result_2}'")
    
    test_case_3 = []
    result_3 = manipulator.merge_fragments(test_case_3)
    print(f"Test Case 3 (Empty List): '{result_3}'")
    
    test_case_4 = ["a", "b", "c"]
    result_4 = manipulator.merge_fragments(test_case_4)
    print(f"Test Case 4: '{result_4}'")