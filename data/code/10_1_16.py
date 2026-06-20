def reverse_words_preserving_whitespace(text: str) -> str:
    if not text:
        return text
    tokens = []
    buffer = []
    is_space = text[0].isspace()
    for char in text:
        current_is_space = char.isspace()
        if current_is_space == is_space:
            buffer.append(char)
        else:
            tokens.append(''.join(buffer))
            buffer = [char]
            is_space = current_is_space
    if buffer:
        tokens.append(''.join(buffer))
    word_tokens = []
    sep_tokens = []
    for token in tokens:
        if token and token[0].isspace():
            sep_tokens.append(token)
        else:
            word_tokens.append(token)
    word_tokens.reverse()
    result_tokens = []
    word_idx = 0
    for token in tokens:
        if token and token[0].isspace():
            result_tokens.append(token)
        else:
            if word_idx < len(word_tokens):
                result_tokens.append(word_tokens[word_idx])
                word_idx += 1
            else:
                result_tokens.append(token)
    return ''.join(result_tokens)

class SentenceReverser:
    def __init__(self, original: str):
        self.original = original
        self._cached_reversed = None

    def get_reversed(self) -> str:
        if self._cached_reversed is None:
            self._cached_reversed = reverse_words_preserving_whitespace(self.original)
        return self._cached_reversed

    def get_original(self) -> str:
        return self.original

if __name__ == '__main__':
    sample_text = "   Hello   World  from  Python    "
    print(reverse_words_preserving_whitespace(sample_text))
    reverser = SentenceReverser(sample_text)
    print(reverser.get_reversed())
    print(reverser.get_original())
    print(reverse_words_preserving_whitespace("A"))
    print(reverse_words_preserving_whitespace("  "))
    print(reverse_words_preserving_whitespace(""))