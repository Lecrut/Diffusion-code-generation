from functools import reduce

class LongestStringFinder:
    @staticmethod
    def is_string(item):
        return isinstance(item, str)
    
    @staticmethod
    def longer_string(str1, str2):
        return str1 if len(str1) > len(str2) else str2
    
    @classmethod
    def find_longest_string(cls, data):
        return reduce(cls.longer_string, filter(cls.is_string, data), "")

if __name__ == '__main__':
    sample_list = ["apple", "banana", "kiwi", "strawberry", "grape"]
    result = LongestStringFinder.find_longest_string(sample_list)
    print(result)
    
    sample_list_2 = ["short", "longer", "longest_one", "medium"]
    result_2 = LongestStringFinder.find_longest_string(sample_list_2)
    print(result_2)