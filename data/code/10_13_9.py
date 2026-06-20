import re

def reverse_words(sentence: str) -> str:
    if not sentence:
        return sentence
    
    word_pattern = re.compile(r'\S+')
    space_pattern = re.compile(r'\s+')
    
    words = word_pattern.findall(sentence)
    words.reverse()
    
    space_matches = list(space_pattern.finditer(sentence))
    
    result = []
    word_idx = 0
    
    for i, char in enumerate(sentence):
        if space_pattern.match(char):
            match = space_pattern.match(sentence[i:])
            if match:
                result.append(match.group())
                i += len(match.group()) - 1
                if i >= len(sentence):
                    break
            else:
                result.append(char)
        else:
            if word_idx < len(words):
                result.append(words[word_idx])
                word_idx += 1
                
    if word_idx < len(words):
        remainder = sentence.find(words[word_idx])
        if remainder != -1:
            result.append(sentence[remainder:])
        else:
            result.append(words[word_idx])
            
    if word_idx < len(words):
        remaining_words = words[word_idx:]
        for w in remaining_words:
            result.append(w)
            
    return ''.join(result)

if __name__ == '__main__':
    sample_sentence = "Hello   World  Python"
    reversed_sentence = reverse_words(sample_sentence)
    print(reversed_sentence)