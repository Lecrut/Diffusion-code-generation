def reverse_sentence_in_place(sentence):
    words = sentence.split()
    for i in range(len(words) // 2):
        words[i], words[~i] = words[~i], words[i]
    return ' '.join(words)

if __name__ == '__main__':
    test_cases = [
        "Hello world",
        "Python is fun",
        "Reverse this sentence",
        "A man a plan a canal Panama"
    ]
    
    for case in test_cases:
        reversed_case = reverse_sentence_in_place(case)
        print(reversed_case)