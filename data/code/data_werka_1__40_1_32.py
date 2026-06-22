def get_first_letters(text):
    words = text.split()
    return [word[0] for word in words if word]

if __name__ == '__main__':
    sample_string = "An optimized approach to solving problems"
    result = get_first_letters(sample_string)
    print(result)