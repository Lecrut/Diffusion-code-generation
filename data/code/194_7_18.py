from functools import reduce

def find_longest_string(strings):
    return reduce(lambda x, y: x if len(x) > len(y) else y, strings)

if __name__ == '__main__':
    sample_list = ["apple", "banana", "kiwi", "strawberry", "grape"]
    longest_string = find_longest_string(sample_list)
    print(longest_string)
    
    sample_list_2 = ["short", "longer", "longest_one", "medium"]
    longest_string_2 = find_longest_string(sample_list_2)
    print(longest_string_2)