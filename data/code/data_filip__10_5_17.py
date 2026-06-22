import re

def reverse_words(sentence):
    tokens = re.findall(r'\S+|\s+', sentence)
    non_whitespace_tokens = [t for t in tokens if not t.isspace()]
    non_whitespace_tokens.reverse()
    result_tokens = []
    ws_iter = iter(non_whitespace_tokens)
    token_list = []
    for t in tokens:
        if t.isspace():
            token_list.append(t)
        else:
            token_list.append(next(ws_iter))
    return ''.join(token_list)

if __name__ == '__main__':
    sample_input = "Hello   world\tthis is\t\t  a   test"
    print(reverse_words(sample_input))
    empty_test = ""
    print(reverse_words(empty_test))
    single_word = "One"
    print(reverse_words(single_word))