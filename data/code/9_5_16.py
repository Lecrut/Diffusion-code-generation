def trim_whitespace(text):
    return text.strip()

if __name__ == '__main__':
    sample = "   \t\n  hello world  \t\n  "
    print(trim_whitespace(sample))