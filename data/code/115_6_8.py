class Divider:
    def __init__(self, pairs):
        self.pairs = pairs

    def divide(self):
        for num1, num2 in self.pairs:
            if num2 == 0:
                raise ValueError("Division by zero is not allowed")
            yield num1 / num2

if __name__ == '__main__':
    sample_pairs = [(4, 2), (9, 3), (10, 5)]
    divider_instance = Divider(sample_pairs)
    for result in divider_instance.divide():
        print(result)