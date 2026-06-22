def reverse_words_preserving_whitespace(text: str) -> str:
    words = [w for w in text.split() if w]
    words.reverse()
    parts = text.split(' ')
    word_indices = [i for i, p in enumerate(parts) if p]
    word_iter = iter(words)
    result = list(text)
    for i in word_indices:
        if i == 0:
            start = 0
        else:
            start = word_indices[word_indices.index(i) - 1] + len(parts[word_indices[word_indices.index(i) - 1]]) + 1
        length = len(parts[i])
        new_word = next(word_iter)
        for j in range(length):
            if start + j < len(text):
                result[start + j] = new_word[j]
    return ''.join(result)

def reverse_words_preserving_whitespace_v2(text: str) -> str:
    import re
    words = re.findall(r'\S+', text)
    words.reverse()
    parts = re.split(r'(\s+)', text)
    result = []
    word_idx = 0
    for part in parts:
        if part.strip():
            result.append(words[word_idx])
            word_idx += 1
        else:
            result.append(part)
    return ''.join(result)

if __name__ == '__main__':
    sample_text = "  Hello   world! This is a test.  "
    result = reverse_words_preserving_whitespace_v2(sample_text)
    print(result)