class FibonacciGenerator:
    def __init__(self):
        self.sequence = []
        self.current_index = 0
        self.a = 0
        self.b = 1
        self._generated = 0

    def generate_n(self, n):
        while self._generated < n:
            if self._generated == 0:
                self.sequence.append(self.a)
            elif self._generated == 1:
                self.sequence.append(self.b)
            else:
                next_val = self.a + self.b
                self.sequence.append(next_val)
                self.a = self.b
                self.b = next_val
            self._generated += 1
        return self.sequence[:n]

    def get_next(self):
        if self._generated == 0:
            val = self.a
            self._generated += 1
            return val
        elif self._generated == 1:
            val = self.b
            self._generated += 1
            return val
        else:
            next_val = self.a + self.b
            self.a = self.b
            self.b = next_val
            self._generated += 1
            return next_val

    def reset(self):
        self.sequence = []
        self.current_index = 0
        self.a = 0
        self.b = 1
        self._generated = 0

if __name__ == '__main__':
    generator = FibonacciGenerator()
    first_150 = generator.generate_n(150)
    print(first_150)