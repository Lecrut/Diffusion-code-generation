def count_special_characters(text):
    special_count = 0
    for char in text:
        if not char.isalnum() and not char.isspace():
            special_count += 1
    return special_count, special_count > 0

if __name__ == '__main__':
    sample_string = "Hello, World! 123 @#"
    count, has_special = count_special_characters(sample_string)
    print(count)
    print(has_special)