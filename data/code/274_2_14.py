def reverse_strings(string_list):
    if not all(isinstance(item, str) for item in string_list):
        raise ValueError("All elements must be strings")
    
    reversed_list = [string[::-1] for string in string_list]
    return reversed_list

if __name__ == '__main__':
    sample_values = ["python", "programming", "is", "fun"]
    try:
        reversed_values = reverse_strings(sample_values)
        for value in reversed_values:
            print(value)
    except ValueError as e:
        print(e)