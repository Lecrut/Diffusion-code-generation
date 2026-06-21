from functools import reduce

def find_longest_string(strings):
    if not all(isinstance(s, str) for s in strings):
        raise ValueError("All elements must be strings")
    return reduce(lambda x, y: x if len(x) > len(y) else y, strings)

if __name__ == '__main__':
    sample_list = ["apple", "banana", "kiwi", "strawberry", "grape"]
    print(find_longest_string(sample_list))
    
    sample_list_2 = ["short", "longer", "longest_one", "medium"]
    print(find_longest_string(sample_list_2))