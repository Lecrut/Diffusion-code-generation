class MultiplicationTableGenerator:
    def __init__(self, base_number):
        self.base_number = base_number
        self._limit = 10

    def generate(self):
        result = {}
        current = 1
        while current <= self._limit:
            result[current] = self.base_number * current
            current += 1
        return result

    def get_item(self, multiplier):
        if 1 <= multiplier <= self._limit:
            return self.base_number * multiplier
        raise ValueError("Multiplier out of range")

if __name__ == '__main__':
    generator = MultiplicationTableGenerator(6)
    full_table = generator.generate()
    print(full_table)
    print(generator.get_item(5))
    print(generator.get_item(10))