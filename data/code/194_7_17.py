from functools import reduce

MAX_LENGTH = float('-inf')

def find_longest_string(strings):
    if not strings:
        return None
    longest = reduce(lambda x, y: y if len(y) > len(x) else x, strings)
    return longest

if __name__ == '__main__':
    sample_list = ["apple", "banana", "kiwi", "strawberry", "grape"]
    result = find_longest_string(sample_list)
    print(result)