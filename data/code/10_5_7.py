import re

def reverse_words(sentence):
    parts = re.split(r'(\s+)', sentence)
    words = [part for part in parts if part and not part.isspace()]
    separators = [part for part in parts if part and part.isspace()]
    
    words.reverse()
    
    result_parts = []
    word_index = 0
    sep_index = 0
    
    for part in parts:
        if part and part.isspace():
            result_parts.append(separators[sep_index])
            sep_index += 1
        elif part:
            result_parts.append(words[word_index])
            word_index += 1
            
    return ''.join(result_parts)

if __name__ == '__main__':
    sample_sentence = "Hello   world  this\tis\t\ta test"
    reversed_sentence = reverse_words(sample_sentence)
    print(reversed_sentence)