def find_repeated_letters(sentence):
    counts = {}
    for char in sentence.lower():
        if char.isalpha():
            counts[char] = counts.get(char, 0) + 1
    repeated = [char for char, count in counts.items() if count > 1]
    return repeated

if __name__ == '__main__':
    sample_sentence = "Hello World"
    result = find_repeated_letters(sample_sentence)
    print(result)