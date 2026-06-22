def contains_special_characters(text):
    special_symbols = set('!@#$%^&*()_+-=[]{}|;:,.<>?/~`')
    text_chars = set(text)
    intersection = special_symbols & text_chars
    return len(intersection) > 0

if __name__ == '__main__':
    sample1 = "hello world"
    sample2 = "hello@world!"
    sample3 = "no_special_chars_here"
    sample4 = "has#special"

    print(contains_special_characters(sample1))
    print(contains_special_characters(sample2))
    print(contains_special_characters(sample3))
    print(contains_special_characters(sample4))