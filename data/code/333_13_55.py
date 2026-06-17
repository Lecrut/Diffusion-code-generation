def extract_first_letters(text):
    return [word[0] for word in text.split() if word]
if __name__ == '__main__':
    sample_text = "Python Programming is Fun"
    result = extract_first_letters(sample_text)
    print("".join(result))