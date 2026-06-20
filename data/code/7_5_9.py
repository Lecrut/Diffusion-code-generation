def count_special_chars(s: str) -> int:
    count = 0
    for char in s:
        if not char.isalnum() and not char.isspace():
            count += 1
    return count

def has_special_chars(s: str) -> bool:
    return count_special_chars(s) > 0

if __name__ == '__main__':
    sample_string = "Hello, World! 123"
    result_count = count_special_chars(sample_string)
    result_flag = has_special_chars(sample_string)
    print(result_count)
    print(result_flag)