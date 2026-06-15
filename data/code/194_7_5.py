class MyList:
    def __init__(self, data):
        self.data = data
    def find_longest_string(self):
        if not self.data:
            return None
        longest_string = ""
        for item in self.data:
            if isinstance(item, str) and len(item) > len(longest_string):
                longest_string = item
        return longest_string
if __name__ == '__main__':
    list1 = MyList(["apple", "banana", "kiwi", "strawberry"])
    print(f"Longest string in list1: {list1.find_longest_string()}")
    list2 = MyList(["short", "longer", "longest", "test"])
    print(f"Longest string in list2: {list2.find_longest_string()}")
    list3 = MyList(["one", "two", "three"])
    print(f"Longest string in list3: {list3.find_longest_string()}")
    list4 = MyList([1, 2, 3, "hello"])
    print(f"Longest string in list4: {list4.find_longest_string()}")
    list5 = MyList([])
    print(f"Longest string in list5: {list5.find_longest_string()}")