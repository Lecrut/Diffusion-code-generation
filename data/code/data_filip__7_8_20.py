def count_special_characters(text):
    count = 0
    found = False
    for char in text:
        if char in '!@#$%^&*()-_=+[]{}|;:,.<>?/~`':
            count += 1
            found = True
    return count, found

if __name__ == '__main__':
    sample_text = "Hello, World! 123"
    result_count, result_status = count_special_characters(sample_text)
    print(result_count)
    print(result_status)