def reverse_words_preserve_spacing(s: str) -> str:
    if not s:
        return ''
    words = []
    i = 0
    n = len(s)
    while i < n:
        if s[i] != ' ':
            start = i
            while i < n and s[i] != ' ':
                i += 1
            words.append(s[start:i])
        else:
            i += 1
    words.reverse()
    parts = []
    i = 0
    n = len(s)
    word_list = []
    space_chunks = []
    while i < n:
        if s[i] == ' ':
            start = i
            while i < n and s[i] == ' ':
                i += 1
            space_chunks.append(s[start:i])
        else:
            start = i
            while i < n and s[i] != ' ':
                i += 1
            word_list.append(s[start:i])
    reversed_words = word_list[::-1]
    result = []
    w_idx = 0
    chunks = []
    i = 0
    n = len(s)
    while i < n:
        if s[i] == ' ':
            start = i
            while i < n and s[i] == ' ':
                i += 1
            chunks.append(('space', s[start:i]))
        else:
            start = i
            while i < n and s[i] != ' ':
                i += 1
            chunks.append(('word', s[start:i]))
    rev_words_iter = iter(reversed_words)
    output_chunks = []
    for item_type, content in chunks:
        if item_type == 'word':
            output_chunks.append(next(rev_words_iter))
        else:
            output_chunks.append(content)
    return ''.join(output_chunks)
if __name__ == '__main__':
    sample_str = 'Hello   World  Python'
    result = reverse_words_preserve_spacing(sample_str)
    print(result)