def find_repeated_letters(sentence):
    frequency = {}
    for char in sentence.lower():
        if char.isalpha():
            frequency[char] = frequency.get(char, 0) + 1
    repeated = {char for char, count in frequency.items() if count > 1}
    return sorted(list(repeated))

if __name__ == '__main__':
    sample_sentence = "Hello World"
    result = find_repeated_letters(sample_sentence)
    print(result)