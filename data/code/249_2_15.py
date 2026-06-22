def max_lexicographical_element(strings):
    if not strings:
        return None
    return max(strings)

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry"]
    print(max_lexicographical_element(sample_strings))