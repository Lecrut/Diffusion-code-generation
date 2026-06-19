class StringManipulator:
    def __init__(self):
        self.delimiters = {
            "space": " ",
            "comma": ",",
            "semicolon": ";"
        }

    def merge_fragments(self, fragments: list[str], delimiter="") -> str:
        if not fragments:
            return ""
        if delimiter in self.delimiters:
            return self.delimiters[delimiter].join(fragments)
        return "".join(fragments)

if __name__ == '__main__':
    manipulator = StringManipulator()
    test_case_1 = ["Hello", "World"]
    result_1 = manipulator.merge_fragments(test_case_1, delimiter="space")
    print(f"Test Case 1: '{result_1}'")

    test_case_2 = ["Python", "is", "fun"]
    result_2 = manipulator.merge_fragments(test_case_2)
    print(f"Test Case 2: '{result_2}'")

    test_case_3 = []
    result_3 = manipulator.merge_fragments(test_case_3, delimiter="comma")
    print(f"Test Case 3 (Empty List): '{result_3}'")

    test_case_4 = ["a", "b", "c"]
    result_4 = manipulator.merge_fragments(test_case_4, delimiter="semicolon")
    print(f"Test Case 4: '{result_4}'")