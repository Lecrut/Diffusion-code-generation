import string

def has_special_characters(text):
    printable = set(string.printable)
    special_chars_found = []
    for char in text:
        if char in printable and not char.isalnum() and char not in string.whitespace:
            special_chars_found.append(char)
    return special_chars_found

if __name__ == '__main__':
    sample_text = "Hello, World! 123 @test"
    result = has_special_characters(sample_text)
    print(result)