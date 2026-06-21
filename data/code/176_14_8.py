def find_letter_sequences(s):
    return {s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1) if s[i:j].isalpha()}

if __name__ == '__main__':
    sample_string = "Hello, 世界!"
    print(find_letter_sequences(sample_string))