def longest_item(lst):
    return max(map(str, lst), key=len)

if __name__ == '__main__':
    sample_list = [123, "hello", 456789, "world", "Python"]
    print(longest_item(sample_list))