def process_sentence(input_sentence):
    result = input_sentence.replace(" ", "")
    print(result)
if __name__ == '__main__':
    sample_sentence = "This is a sample sentence with extra spaces"
    process_sentence(sample_sentence)