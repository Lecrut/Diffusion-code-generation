def remove_spaces(s):
    return ''.join(s.split())

if __name__ == '__main__':
    original_string = "  Python   is  fun! "
    processed_string = remove_spaces(original_string)
    print(processed_string)