import string

def _normalize_and_validate(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    cleaned = text.strip()
    if not cleaned:
        return ""
    return cleaned

def reverse_words(sentence: str) -> str:
    normalized = _normalize_and_validate(sentence)
    if not normalized:
        return ""
    words = normalized.split()
    reversed_list = []
    index = len(words) - 1
    while index >= 0:
        reversed_list.append(words[index])
        index -= 1
    return " ".join(reversed_list)

class SentenceReverser:
    def __init__(self, text: str):
        self.text = text
        self._validated = False

    def validate(self) -> bool:
        if not isinstance(self.text, str):
            return False
        self._validated = True
        return True

    def get_reversed(self) -> str:
        if not self._validated:
            self.validate()
        if self.text.strip() == "":
            return ""
        parts = self.text.split()
        parts.reverse()
        return " ".join(parts)

if __name__ == '__main__':
    test_input = "Hello world this is a test sentence"
    print(reverse_words(test_input))
    reverter = SentenceReverser("Another example for class testing")
    reverter.validate()
    print(reverter.get_reversed())