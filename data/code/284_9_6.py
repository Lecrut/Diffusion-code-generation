def reverse_words_in_string(s):
    word_map = {word: word[::-1] for word in s.split()}
    reversed_string = ' '.join(word_map[word] for word in s.split())
    return reversed_string

if __name__ == '__main__':
    sample_input = "Python is fun to learn"
    print(reverse_words_in_string(sample_input))