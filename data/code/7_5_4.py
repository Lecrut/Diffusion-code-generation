def count_special_characters(text):
    special_count = 0
    for char in text:
        if not char.isalnum() and not char.isspace():
            special_count += 1
    is_special = special_count > 0
    return special_count, is_special

if __name__ == '__main__':
    sample_string = "Hello@World#2024!"
    count, flag = count_special_characters(sample_string)
    print(count)
    print(flag)