class StringManipulator:

    def merge_fragments(self, fragments: list[str]) -> str:
        if not fragments:
            return ''
        return ''.join(fragments)
if __name__ == '__main__':
    manipulator = StringManipulator()
    test_case_1 = ['Hello', ' ', 'World']
    result_1 = manipulator.merge_fragments(test_case_1)
    print(f"Test Case 1 Result: '{result_1}'")
    test_case_2 = ['Python', '   ', 'is', 'fun']
    result_2 = manipulator.merge_fragments(test_case_2)
    print(f"Test Case 2 Result: '{result_2}'")
    test_case_3 = []
    result_3 = manipulator.merge_fragments(test_case_3)
    print(f"Test Case 3 (Empty List) Result: '{result_3}'")
    test_case_4 = ['a', 'b', 'c', 'd']
    result_4 = manipulator.merge_fragments(test_case_4)
    print(f"Test Case 4 Result: '{result_4}'")
    test_case_5 = ['Hi', ' ', 'there', '!']
    result_5 = manipulator.merge_fragments(test_case_5)
    print(f"Test Case 5 Result: '{result_5}'")