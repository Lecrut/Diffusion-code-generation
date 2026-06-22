def remove_vowels(text):
    if not text:
        return ""
    vowels = set('aeiou')
    return "".join(char for char in text if char.lower() not in vowels)

if __name__ == '__main__':
    sample_input = "Programming is fun and easy"
    output = remove_vowels(sample_input)
    print(output)