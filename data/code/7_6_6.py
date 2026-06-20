def has_special_characters(text):
    for char in text:
        if not char.isalnum() and not char.isspace():
            return True
    return False

if __name__ == '__main__':
    sample_values = [
        "hello world",
        "hello world!",
        "12345",
        "test@email.com",
        "   ",
        "no_special",
        "has#special"
    ]
    for sample in sample_values:
        result = has_special_characters(sample)
        print(result)