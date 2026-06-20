def has_special_characters(text):
    special_characters = set()
    for i in range(32, 127):
        if chr(i).isalnum():
            continue
        if chr(i) == ' ':
            continue
        special_characters.add(chr(i))

    for char in text:
        if char in special_characters:
            return True
    return False

if __name__ == '__main__':
    sample_values = ['hello', 'hello!', 'world#1', '12345', 'test@123']
    for value in sample_values:
        result = has_special_characters(value)
        print(result)