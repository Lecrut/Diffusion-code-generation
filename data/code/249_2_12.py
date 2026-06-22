def max_lexicographical(lst):
    if not all(isinstance(item, str) for item in lst):
        raise ValueError("All elements in the list must be strings.")
    return max(lst)

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry"]
    print(max_lexicographical(sample_list))