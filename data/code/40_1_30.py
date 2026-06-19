def get_first_letters(text):
    return [word[0] for word in text.split() if word]

if __name__ == '__main__':
    SAMPLE_STRING = "Implementing optimized function using list comprehension"
    result = get_first_letters(SAMPLE_STRING)
    print(result)