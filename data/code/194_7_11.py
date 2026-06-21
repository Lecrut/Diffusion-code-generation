from functools import reduce

class StringFinder:
    def __init__(self, data):
        self.data = data
    
    def find_longest_string(self):
        return reduce(lambda x, y: x if len(x) > len(y) else y, filter(str.isalpha, self.data), "")

if __name__ == '__main__':
    sample_list = ["apple", "banana", "kiwi", "strawberry", "grape"]
    string_finder = StringFinder(sample_list)
    result = string_finder.find_longest_string()
    print(result)
    
    sample_list_2 = ["short", "longer", "longest_one", "medium"]
    string_finder_2 = StringFinder(sample_list_2)
    result_2 = string_finder_2.find_longest_string()
    print(result_2)