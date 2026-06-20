def has_special_chars(text):
    for char in text:
        if not char.isalnum() and char != " ":
            return True
    return False

if __name__ == '__main__':
    sample_1 = "Hello World 123"
    sample_2 = "Error@404"
    print(has_special_chars(sample_1))
    print(has_special_chars(sample_2))