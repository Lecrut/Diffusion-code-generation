def check_special_characters(text):
    special_characters = set()
    for char in text:
        ascii_value = ord(char)
        if 32 <= ascii_value <= 126:
            if not char.isalnum() and not char.isspace():
                special_characters.add(char)
    return sorted(special_characters)

if __name__ == '__main__':
    sample_text = "Hello, World! @Python#2023"
    result = check_special_characters(sample_text)
    print(result)