def is_consonant(char):
    return char.isalpha() and char.lower() not in 'aeiou'

def count_consonants(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    filtered_chars = [char for char in text if is_consonant(char)]
    return len(filtered_chars)

if __name__ == '__main__':
    sample_text = "Python 3.9 is awesome!"
    result = count_consonants(sample_text)
    print(result)