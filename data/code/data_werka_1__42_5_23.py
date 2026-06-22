class StringManipulator:
    def __init__(self):
        self.fragments = []

    def add_fragment(self, fragment: str):
        self.fragments.append(fragment)

    def merge_fragments(self) -> str:
        if not self.fragments:
            return ""
        return "".join(self.fragments)

if __name__ == '__main__':
    manipulator = StringManipulator()
    
    test_case_1 = ["Hello", " ", "World"]
    for fragment in test_case_1:
        manipulator.add_fragment(fragment)
    result_1 = manipulator.merge_fragments()
    print(f"Test Case 1: '{result_1}'")
    
    test_case_2 = ["Python", "is", "fun"]
    for fragment in test_case_2:
        manipulator.add_fragment(fragment)
    result_2 = manipulator.merge_fragments()
    print(f"Test Case 2: '{result_2}'")
    
    test_case_3 = []
    for fragment in test_case_3:
        manipulator.add_fragment(fragment)
    result_3 = manipulator.merge_fragments()
    print(f"Test Case 3 (Empty List): '{result_3}'")
    
    test_case_4 = ["a", "b", "c", "d"]
    for fragment in test_case_4:
        manipulator.add_fragment(fragment)
    result_4 = manipulator.merge_fragments()
    print(f"Test Case 4: '{result_4}'")