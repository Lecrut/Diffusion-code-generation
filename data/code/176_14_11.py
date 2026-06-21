def find_letter_sequences(s):
    sequences = set()
    start = 0
    for i in range(len(s)):
        if not s[i].isalpha():
            if start < i:
                sequences.add(s[start:i])
            start = i + 1
    if start < len(s):
        sequences.add(s[start:])
    return sequences

if __name__ == '__main__':
    sample_string = "Hello, 世界! Привет!"
    print(find_letter_sequences(sample_string))