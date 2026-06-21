def longest_item(lst):
    return max(map(str, lst), key=len)

if __name__ == '__main__':
    sample_list = ['apple', 12345, 'banana', {'key': 'value'}, [1, 2, 3]]
    print(longest_item(sample_list))