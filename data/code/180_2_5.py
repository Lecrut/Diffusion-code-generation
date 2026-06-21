import string

def is_word_in_dictionary(word, dictionary):
    stripped_word = word.strip(string.punctuation).lower()
    return stripped_word in dictionary

if __name__ == '__main__':
    sample_word = "Hello!"
    sample_dictionary = {"hello", "world"}
    print(is_word_in_dictionary(sample_word, sample_dictionary))