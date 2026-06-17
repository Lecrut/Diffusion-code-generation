def process_sentence(sentence):
    result = sentence.replace(" ", "")
    print(result)
if __name__ == '__main__':
    sample_sentence = "This is a sample sentence with extra spaces"
    process_sentence(sample_sentence)