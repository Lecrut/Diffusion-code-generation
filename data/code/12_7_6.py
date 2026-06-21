def is_pure_integer_string(formatted_str):
    remove_chars = "-+"
    remaining = formatted_str.translate(str.maketrans('', '', remove_chars))
    if len(remaining) == 0:
        return False
    for char in remaining:
        if not char.isdigit():
            return False
    return True

if __name__ == '__main__':
    sample1 = "12345"
    sample2 = "-567"
    sample3 = "+890"
    sample4 = "12.34"
    sample5 = "abc"
    sample6 = "12a34"
    sample7 = "  100  "
    sample8 = ""
    sample9 = "--123"
    sample10 = "007"
    
    results = [
        is_pure_integer_string(sample1),
        is_pure_integer_string(sample2),
        is_pure_integer_string(sample3),
        is_pure_integer_string(sample4),
        is_pure_integer_string(sample5),
        is_pure_integer_string(sample6),
        is_pure_integer_string(sample7),
        is_pure_integer_string(sample8),
        is_pure_integer_string(sample9),
        is_pure_integer_string(sample10)
    ]
    print(results)