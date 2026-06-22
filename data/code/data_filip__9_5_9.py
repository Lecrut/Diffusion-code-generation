def trim_string(text):
    return text.strip()

if __name__ == '__main__':
    sample_string = "   hello   world   "
    result = trim_string(sample_string)
    print(result)