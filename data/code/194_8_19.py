def longest_item(lst):
    return max(map(str, lst), key=len)

if __name__ == '__main__':
    sample_list = [123, "hello", 4567890, "world"]
    print(longest_item(sample_list))