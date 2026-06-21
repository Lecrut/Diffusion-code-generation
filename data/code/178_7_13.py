def split_text_into_tokens(text):
    tokens = text.split()
    return tokens

if __name__ == '__main__':
    sample_text = "This is   a   sample\ntext for\nword extraction. This\ttext contains some repeated words, like this and that. Sample is important."
    token_list = split_text_into_tokens(sample_text)
    print(token_list)