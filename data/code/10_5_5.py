import re

def reverse_words(sentence: str) -> str:
    parts = re.split(r'(\s+)', sentence)
    words = []
    separators = []
    for item in parts:
        if item:
            if item.isspace():
                separators.append(item)
            else:
                words.append(item)
    words.reverse()
    result = []
    word_idx = 0
    sep_idx = 0
    for item in parts:
        if item and item.isspace():
            result.append(item)
        elif item:
            result.append(words[word_idx])
            word_idx += 1
    return "".join(result)

if __name__ == '__main__':
    test_string = "  Hello   World  from  Python   "
    reversed_sentence = reverse_words(test_string)
    print(reversed_sentence)
    test_string_2 = "One\t\tTwo\n\nThree"
    reversed_sentence_2 = reverse_words(test_string_2)
    print(reversed_sentence_2)