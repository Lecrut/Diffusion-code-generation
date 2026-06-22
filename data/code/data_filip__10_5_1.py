import re

def reverse_words_in_sentence(sentence):
    words = re.split(r'(\s+)', sentence)
    word_list = [word for word in words if not re.match(r'^\s+$', word) and word != '']
    reversed_words = word_list[::-1]
    result = ''.join([w if re.match(r'^\s+$', w) else reversed_words.pop(0) for w in words if re.match(r'^\s+$', w) or w != ''])
    if not result and not word_list:
        return sentence
    return result

if __name__ == '__main__':
    sample1 = "Hello World"
    sample2 = "  Hello   World  "
    sample3 = "One\tTwo\nThree"
    sample4 = ""
    sample5 = "   "
    print(reverse_words_in_sentence(sample1))
    print(reverse_words_in_sentence(sample2))
    print(reverse_words_in_sentence(sample3))
    print(reverse_words_in_sentence(sample4))
    print(reverse_words_in_sentence(sample5))