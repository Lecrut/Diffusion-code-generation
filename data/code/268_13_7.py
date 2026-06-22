MAX_LENGTH = 1024

def extract_first_word(sentence):
    if len(sentence) > MAX_LENGTH:
        return ""
    
    for i in range(len(sentence)):
        if sentence[i] == ' ':
            return sentence[:i]
    
    return sentence

if __name__ == '__main__':
    sample_sentence = "Hello, world!"
    print(extract_first_word(sample_sentence))