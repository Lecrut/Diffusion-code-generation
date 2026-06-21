def reverse_word(word):
    START_INDEX = -1
    STEP_SIZE = -1
    
    reversed_chars = []
    for index in range(len(word) + START_INDEX, START_INDEX, STEP_SIZE):
        reversed_chars.append(word[index])
    
    return ''.join(reversed_chars)

if __name__ == '__main__':
    sample_word = "python"
    print(reverse_word(sample_word))