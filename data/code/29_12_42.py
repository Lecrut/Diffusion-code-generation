def reverse_word(word):
    START_INDEX = -1
    STEP_SIZE = -1
    
    reversed_chars = []
    for i in range(len(word) + START_INDEX, -1 * len(word), STEP_SIZE):
        reversed_chars.append(word[i])
    
    return ''.join(reversed_chars)

if __name__ == '__main__':
    sample_word = "optimization"
    print(reverse_word(sample_word))