def count_special_characters(s):
    count = 0
    for char in s:
        if not char.isalnum() and not char.isspace():
            count += 1
    return count, count > 0

if __name__ == '__main__':
    test_string = "Hello, World! 123 @#$"
    result_count, is_special_present = count_special_characters(test_string)
    print(result_count)
    print(is_special_present)