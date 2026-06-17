def extract_first_letters(text):
    words = text.split()
    if not words:
        return ""
    result_chars = []
    for word in words:
        char = word[0]
        result_chars.append(char)
    return ''.join(result_chars)
def main():
    sample_input = "Hello World Python Programming"
    output = extract_first_letters(sample_input)
    print(output)
if __name__ == '__main__':
    main()