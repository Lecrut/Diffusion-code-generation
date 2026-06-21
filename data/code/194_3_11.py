if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry"]
    if isinstance(sample_list, list) and all(isinstance(item, str) for item in sample_list):
        longest_element = max(sample_list, key=len)
        print(longest_element)