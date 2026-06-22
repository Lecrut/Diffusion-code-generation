def find_max_lexicographical(lst):
    if not lst:
        return None
    max_element = max(lst)
    return max_element

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry"]
    print(find_max_lexicographical(sample_list))