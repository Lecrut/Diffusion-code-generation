def get_first_letters(text):
    words = text.split()
    if not words:
        return []
    return [word[0] for word in words]

if __name__ == '__main__':
    sample_string = "An optimized function implementation"
    result = get_first_letters(sample_string)
    print(result)