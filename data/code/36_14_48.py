def reverse_sentence(sentence):
    def split_into_words(s):
        return s.split()
    
    def reverse_list(lst):
        return lst[::-1]
    
    words = split_into_words(sentence)
    reversed_words = reverse_list(words)
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

if __name__ == '__main__':
    sample_sentence = "Implementing a new solution"
    print(reverse_sentence(sample_sentence))