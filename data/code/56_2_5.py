class MultiplicationTableGenerator:
    def __init__(self, base_number):
        self.base_number = base_number

    def generate_rows(self, count=10):
        for i in range(1, count + 1):
            yield self.base_number * i

    def get_row_string(self, index):
        if 1 <= index <= 10:
            return f"{self.base_number} x {index} = {self.base_number * index}"
        return None

if __name__ == '__main__':
    generator = MultiplicationTableGenerator(12)
    numeric_rows = list(generator.generate_rows(5))
    print(numeric_rows)
    formatted_row = generator.get_row_string(7)
    print(formatted_row)
    print(generator.get_row_string(3))