class StringManipulator:
    def merge_fragments(self, fragments: list[str]) -> str:
        if not fragments:
            return ""
        return "".join(fragments)
if __name__ == '__main__':
    manipulator = StringManipulator()
    list1 = ["Hello", " ", "World"]
    result1 = manipulator.merge_fragments(list1)
    print(f"Input: {list1}")
    print(f"Result: '{result1}'")
    list2 = ["Python", " ", "is", "fun"]
    result2 = manipulator.merge_fragments(list2)
    print(f"Input: {list2}")
    print(f"Result: '{result2}'")
    list3 = []
    result3 = manipulator.merge_fragments(list3)
    print(f"Input: {list3}")
    print(f"Result: '{result3}'")
    list4 = ["Single"]
    result4 = manipulator.merge_fragments(list4)
    print(f"Input: {list4}")
    print(f"Result: '{result4}'")