import re

def reverse_words(sentence: str) -> str:
    words = re.findall(r'\S+', sentence)
    words.reverse()
    spaces = re.findall(r'\s+', sentence)
    result = []
    word_idx = 0
    space_idx = 0
    
    i = 0
    while i < len(sentence):
        if i < len(spaces):
            result.append(spaces[space_idx])
            space_idx += 1
            i += len(spaces[space_idx - 1])
        else:
            if word_idx < len(words):
                result.append(words[word_idx])
                word_idx += 1
            else:
                break
        i += 1
    
    if word_idx < len(words):
        result.append(words[word_idx])
        
    return ''.join(result)

if __name__ == '__main__':
    print(reverse_words("Hello   World"))
    print(reverse_words("  Space at start"))
    print(reverse_words("No space"))
    print(reverse_words(""))