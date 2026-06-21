def longest_item(lst):
    return max(lst, key=str)

if __name__ == '__main__':
    sample = [123, "hello", 456789, "world", [], {}, (1, 2)]
    print(longest_item(sample))