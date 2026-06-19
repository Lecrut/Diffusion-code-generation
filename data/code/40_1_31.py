def get_first_letters(text):
    words = text.split()
    first_letters = [word[0] for word in words if word]
    return first_letters

if __name__ == '__main__':
    sample_string = "An optimized function for getting first letters"
    result = get_first_letters(sample_string)
    print(result)