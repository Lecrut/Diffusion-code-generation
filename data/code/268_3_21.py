def extract_initial_word(sentence):
    word_list = sentence.split()
    first_word = word_list[0] if word_list else ''
    return first_word

if __name__ == '__main__':
    sample_text = "Good morning from Alibaba Cloud"
    print(extract_initial_word(sample_text))