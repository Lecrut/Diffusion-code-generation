import string

def count_special_characters(text):
    special_chars = set(string.punctuation) | {"!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "[", "]", "{", "}", "|", "\\", ":", ";", "\"", "'", "<", ">", ",", ".", "/", "?", "`", "~"}
    count = 0
    for char in text:
        if char in special_chars:
            count += 1
    return count > 0, count

if __name__ == '__main__':
    result, count = count_special_characters("Hello, World!")
    print(result, count)