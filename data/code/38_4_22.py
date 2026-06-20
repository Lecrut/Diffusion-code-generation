def find_repeated_letters(sentence):
    letters_only = [char.lower() for char in sentence if char.isalpha()]
    counts = {}
    for char in letters_only:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    repeated = [char for char, count in counts.items() if count > 1]
    return repeated

if __name__ == '__main__':
    sentence = "Hello World"
    result = find_repeated_letters(sentence)
    print(result)