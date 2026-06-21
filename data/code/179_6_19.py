def reverse_words(input_text):
    words = input_text.split()
    reversed_list = []
    for word in words:
        reversed_word = ''
        for char in word:
            reversed_word = char + reversed_word
        reversed_list.append(reversed_word)
    return ' '.join(reversed_list)

if __name__ == '__main__':
    sample_sentence = "Python is fun to learn"
    print(reverse_words(sample_sentence))