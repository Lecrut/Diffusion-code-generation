def longest_item(lst):
    return max(lst, key=str)

if __name__ == '__main__':
    sample_list = ['apple', 1234567890, True, 'banana']
    print(longest_item(sample_list))