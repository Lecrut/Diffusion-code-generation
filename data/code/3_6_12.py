def remove_vowels(text):
    return ''.join(filter(lambda char: char.lower() not in 'aeiou', text))

if __name__ == '__main__':
    sample_string = "Hello World"
    result = remove_vowels(sample_string)
    print(result)