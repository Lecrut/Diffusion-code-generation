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
    sample_list = ["apple", "banana", "kiwi", "strawberry", "grape"]
    my_list = MyList(sample_list)
    result = my_list.find_longest_string()
    print(result)
    sample_list_2 = ["short", "longer", "longestword", "medium"]
    my_list_2 = MyList(sample_list_2)
    result_2 = my_list_2.find_longest_string()
    print(result_2)
    sample_list_3 = [1, 2, 3, "a", "bb", "ccc"]
    my_list_3 = MyList(sample_list_3)
    result_3 = my_list_3.find_longest_string()
    print(result_3)
    sample_list_4 = []
    my_list_4 = MyList(sample_list_4)
    result_4 = my_list_4.find_longest_string()
    print(result_4)