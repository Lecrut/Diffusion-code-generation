def reverse_strings(input_list):
    if not all(isinstance(item, str) for item in input_list):
        raise ValueError("All elements in the list must be strings")
    
    return [item[::-1] for item in input_list]

if __name__ == '__main__':
    sample_values = ["hello", "world", "!"]
    print(reverse_strings(sample_values))