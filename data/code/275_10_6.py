def is_valid_string(s):
    return isinstance(s, str)

def reverse_string(s):
    reversed_str = ''
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

def process_strings(string_list):
    if not all(is_valid_string(item) for item in string_list):
        raise ValueError("All elements in the list must be strings")
    
    for s in string_list:
        print(reverse_string(s))

if __name__ == '__main__':
    sample_values = ["hello", "world", "!"]
    process_strings(sample_values)