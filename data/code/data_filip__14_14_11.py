def has_unique_characters(text):
    sorted_text = sorted(text)
    for i in range(len(sorted_text) - 1):
        if sorted_text[i] == sorted_text[i + 1]:
            return False
    return True

if __name__ == '__main__':
    sample_string = "abcdef"
    result = has_unique_characters(sample_string)
    print(result)

    duplicate_string = "hello"
    duplicate_result = has_unique_characters(duplicate_string)
    print(duplicate_result)