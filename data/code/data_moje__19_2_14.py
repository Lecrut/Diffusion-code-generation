class RandomCharSelector:
    _DEFAULT_VALUE = ""

    @staticmethod
    def _validate_input(text):
        if text is None:
            return RandomCharSelector._DEFAULT_VALUE
        return text

    @staticmethod
    def _compute_index(length):
        import random
        return random.randint(0, length - 1)

    def pick(self, text):
        cleaned = self._validate_input(text)
        if not cleaned:
            return self._DEFAULT_VALUE
        idx = self._compute_index(len(cleaned))
        return cleaned[idx]

if __name__ == '__main__':
    selector = RandomCharSelector()
    sample = "pymath_random"
    char = selector.pick(sample)
    print(char)