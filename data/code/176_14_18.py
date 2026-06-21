def find_letter_sequences(s):
    sequences = set()
    i = 0
    while i < len(s):
        if s[i].isalpha():
            start = i
            while i + 1 < len(s) and s[i + 1].isalpha():
                i += 1
            sequences.add(s[start:i + 1])
        i += 1
    return sequences

if __name__ == '__main__':
    sample_string = "Hello, 世界! Привет"
    print(find_letter_sequences(sample_string))