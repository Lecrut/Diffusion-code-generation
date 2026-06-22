import re

def reverse_words(sentence):
    if not sentence:
        return sentence
    words = re.findall(r'\S+', sentence)
    words.reverse()
    def replacer(match):
        if match.group(1) is not None:
            word_index = int(match.group(0).split('_')[1])
            return words[word_index]
        return match.group(2)
    result = re.sub(r'__(\d+)__(\s+)', replacer, re.sub(r'\S+', '__%d__' % len(words), sentence, count=0))
    word_index = 0
    temp = re.sub(r'__(\d+)__', lambda m: words[word_index], sentence)
    word_index_map = {}
    current_idx = 0
    parts = sentence.split()
    if not parts:
        return sentence
    words_list = list(reversed(parts))
    spaces = re.split(r'\S+', sentence)
    result_parts = []
    for i, part in enumerate(spaces):
        result_parts.append(part)
        if i < len(words_list):
            result_parts.append(words_list[i])
    final_result = "".join(result_parts)
    if sentence.endswith(" ") and not final_result.endswith(" "):
        final_result += " "
    if sentence.startswith(" ") and not final_result.startswith(" "):
        final_result = " " + final_result
    return final_result

if __name__ == '__main__':
    print(reverse_words("Hello World"))
    print(reverse_words("  space   words  "))
    print(reverse_words(""))
    print(reverse_words("one"))