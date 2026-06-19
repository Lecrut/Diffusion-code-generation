def get_first_letters(text):
    words = text.split()
    first_letters = [word[0] for word in words]
    return first_letters

if __name__ == '__main__':
    sample_string = "An example with multiple words"
    result = get_first_letters(sample_string)
    print(result)