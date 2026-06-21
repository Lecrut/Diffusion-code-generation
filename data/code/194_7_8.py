from functools import reduce

def longest_string(strings):
    return reduce(lambda x, y: x if len(x) > len(y) else y, strings)

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    print(longest_string(sample_strings))