class FibonacciGenerator:
    _DEFAULT_COUNT = 100

    def __init__(self, start_a=0, start_b=1):
        self._current = start_a
        self._next = start_b

    def _advance(self):
        current_val = self._current
        self._current, self._next = self._next, self._current + self._next
        return current_val

    def get_terms(self, count=None):
        if count is None:
            count = self._DEFAULT_COUNT
        if count <= 0:
            return []
        terms = []
        for _ in range(count):
            terms.append(self._advance())
        return terms

    def get_single_term(self, index):
        self._current, self._next = 0, 1
        if index < 0:
            return None
        if index == 0:
            return 0
        for _ in range(1, index + 1):
            self._current, self._next = self._next, self._current + self._next
        return self._current

if __name__ == '__main__':
    generator = FibonacciGenerator()
    first_100 = generator.get_terms(100)
    print(first_100)
    tenth_term = generator.get_single_term(9)
    print(tenth_term)