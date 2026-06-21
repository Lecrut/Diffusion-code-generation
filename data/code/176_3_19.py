SENTENCE = "This is a sample sentence for splitting into words."

def split_sentence_into_words(sentence=SENTENCE):
    return sentence.lower().split()

if __name__ == '__main__':
    print(split_sentence_into_words())