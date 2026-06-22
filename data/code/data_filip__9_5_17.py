def trim_string(text):
    return text.strip()

if __name__ == '__main__':
    sample = "   excessive   whitespace   here   "
    print(trim_string(sample))