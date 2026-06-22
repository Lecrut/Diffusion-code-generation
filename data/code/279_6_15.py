def reverse_strings(string_list):
    if not all(isinstance(item, str) for item in string_list):
        raise ValueError("All elements in the list must be strings.")
    
    reversed_list = [s[::-1] for s in string_list]
    return reversed_list

if __name__ == '__main__':
    sample_values = ["hello", "world", "!"]
    try:
        reversed_strings = reverse_strings(sample_values)
        print(reversed_strings)
    except ValueError as e:
        print(e)