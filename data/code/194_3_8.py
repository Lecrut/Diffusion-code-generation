if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry"]
    if not all(isinstance(item, str) for item in sample_list):
        raise ValueError("All elements must be strings")
    
    longest_element = max(sample_list, key=len)
    print(longest_element)