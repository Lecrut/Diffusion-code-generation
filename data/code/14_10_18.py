def has_unique_characters(s):
    return len(s) == len(set(s))
if __name__ == '__main__':
    sample_values = ['abcde', 'hello', 'Python', 'AaBbCc', '12345', '112233']
    for value in sample_values:
        print(f"String '{value}' has unique characters: {has_unique_characters(value)}")