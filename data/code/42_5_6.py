class StringManipulator:
    def merge_fragments(self, fragments):
        if not fragments:
            return ""
        return "".join(fragments)
if __name__ == '__main__':
    manipulator = StringManipulator()
    list1 = ["Hello", " ", "World"]
    result1 = manipulator.merge_fragments(list1)
    print(f"Result 1: '{result1}'")
    list2 = ["Python", "is", "fun"]
    result2 = manipulator.merge_fragments(list2)
    print(f"Result 2: '{result2}'")
    list3 = []
    result3 = manipulator.merge_fragments(list3)
    print(f"Result 3: '{result3}'")
    list4 = ["a", "b", "c"]
    result4 = manipulator.merge_fragments(list4)
    print(f"Result 4: '{result4}'")