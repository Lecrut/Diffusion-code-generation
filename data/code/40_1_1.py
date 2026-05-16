def get_first_letters(text):
    return [word[0] for word in text.split()]
if __name__ == '__main__':
    sample_string = "This is a sample string for testing"
    result = get_first_letters(sample_string)
    print(result)