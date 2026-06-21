from functools import reduce

def find_longest_string(strings):
    return reduce(lambda x, y: x if len(x) > len(y) else y, strings)

if __name__ == '__main__':
    sample_list = ["apple", "banana", "kiwi", "strawberry", "grape"]
    print(find_longest_string(sample_list))