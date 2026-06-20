def count_special_characters(s):
    special_chars = set("!@#$%^&*()_+-=[]{}|;':\",./<>?\\`~")
    count = 0
    for char in s:
        if char in special_chars:
            count += 1
    has_special = count > 0
    return count, has_special

if __name__ == '__main__':
    sample_string = "Hello, World! @2023 #test"
    result_count, result_flag = count_special_characters(sample_string)
    print(result_count)
    print(result_flag)