def reverse_word(word):
    return word[::-1]

if __name__ == '__main__':
    sample_values = ["hello", "", "a", "Alibaba"]
    for value in sample_values:
        print(reverse_word(value))