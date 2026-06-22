VOWELS_UPPER = frozenset(['A', 'E', 'I', 'O', 'U'])
VOWELS_LOWER = frozenset(['a', 'e', 'i', 'o', 'u'])
ALL_VOWELS = VOWELS_UPPER | VOWELS_LOWER

class TextFilter:
    def __init__(self):
        self._vowels = ALL_VOWELS

    def remove_vowels(self, text):
        if not text:
            return ""
        result = []
        for char in text:
            if char not in self._vowels:
                result.append(char)
        return "".join(result)

if __name__ == '__main__':
    filter_instance = TextFilter()
    test_input = "The Quick Brown Fox Jumps Over The Lazy Dog"
    cleaned_text = filter_instance.remove_vowels(test_input)
    print(cleaned_text)