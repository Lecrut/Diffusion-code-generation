def max_lexicographical(lst):
    if not lst:
        raise ValueError("List is empty")
    return max(lst)

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry"]
    print(max_lexicographical(sample_list))