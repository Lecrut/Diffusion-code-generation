def get_first_letters(text):
    return [word[0] for word in text.split() if word]

if __name__ == '__main__':
    sample_string = "Implementing an optimized function"
    result = get_first_letters(sample_string)
    print(result)