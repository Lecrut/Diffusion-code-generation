CHAR_DELIMITER = ' '

def reverse_strings(string_list):
    return [s[::-1] for s in string_list]

if __name__ == '__main__':
    sample_values = ["hello", "world", "!"]
    print(reverse_strings(sample_values))