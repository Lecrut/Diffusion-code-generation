def trim_spaces(text):
    return text.strip()

if __name__ == '__main__':
    sample = "   Hello World   "
    result = trim_spaces(sample)
    print(result)