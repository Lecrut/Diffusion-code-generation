def split_text_into_tokens(text):
    tokens = text.split()
    return tokens

if __name__ == '__main__':
    sample_text = "This  is\ta\nsample   text for word extraction. This text contains some repeated words, like this and that. Sample again."
    tokens_list = split_text_into_tokens(sample_text)
    print(tokens_list)