class FibonacciGenerator:
    def __init__(self):
        self._cache = [0, 1]

    def generate_sequence(self, count):
        if count <= 0:
            return []
        if count == 1:
            return [0]
        
        while len(self._cache) < count:
            next_val = self._cache[-1] + self._cache[-2]
            self._cache.append(next_val)
        
        return self._cache[:count]

if __name__ == '__main__':
    generator = FibonacciGenerator()
    result = generator.generate_sequence(150)
    print(result)