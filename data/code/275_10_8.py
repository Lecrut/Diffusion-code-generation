def reverse_string(s):
    reversed_str = ''
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

def process_strings(string_list):
    if not isinstance(string_list, list) or not all(isinstance(item, str) for item in string_list):
        raise ValueError("Input must be a list of strings")
    
    for s in string_list:
        print(reverse_string(s))

if __name__ == '__main__':
    sample_values = ["hello", "world", "!"]
    process_strings(sample_values)