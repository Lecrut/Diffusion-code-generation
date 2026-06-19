class StringManipulator:
    def merge_fragments(self, fragments: list[str]) -> str:
        if not isinstance(fragments, list):
            raise ValueError("Input must be a list")
        if any(not isinstance(fragment, str) for fragment in fragments):
            raise ValueError("All elements in the list must be strings")
        return "".join(fragments)

if __name__ == '__main__':
    manipulator = StringManipulator()
    
    try:
        test_case_1 = ["Hello", " ", "World"]
        result_1 = manipulator.merge_fragments(test_case_1)
        print(f"Test Case 1: '{result_1}'")
    except ValueError as e:
        print(f"Error in Test Case 1: {e}")
    
    try:
        test_case_2 = ["Python", "is", "fun"]
        result_2 = manipulator.merge_fragments(test_case_2)
        print(f"Test Case 2: '{result_2}'")
    except ValueError as e:
        print(f"Error in Test Case 2: {e}")
    
    try:
        test_case_3 = []
        result_3 = manipulator.merge_fragments(test_case_3)
        print(f"Test Case 3 (Empty List): '{result_3}'")
    except ValueError as e:
        print(f"Error in Test Case 3: {e}")
    
    try:
        test_case_4 = ["a", "b", "c", "d"]
        result_4 = manipulator.merge_fragments(test_case_4)
        print(f"Test Case 4: '{result_4}'")
    except ValueError as e:
        print(f"Error in Test Case 4: {e}")