def find_longest_item(lst):
    if not lst:
        return None
    longest = lst[0]
    for item in lst:
        if len(item) > len(longest):
            longest = item
    return longest

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry', 'date']
    print(find_longest_item(sample_list))