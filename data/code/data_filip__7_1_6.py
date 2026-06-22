def has_special_characters(text):
    printable_ascii = set((chr(i) for i in range(32, 127)))
    for char in text:
        if char in printable_ascii:
            if not char.isalnum() and (not char.isspace()):
                return True
    return False
if __name__ == '__main__':
    samples = ['hello world', 'hello world!', 'abc123', 'test@123', 'no special chars here', 'has#special#chars']
    for sample in samples:
        result = has_special_characters(sample)
        print(result)