class SumGenerator:
    def __init__(self, data):
        self.data = iter(data)

    def next(self):
        try:
            return next(self.data)
        except StopIteration:
            raise ValueError("No more items to sum")

    @staticmethod
    def sum_generator(generator):
        total = 0
        while True:
            try:
                value = generator.next()
                total += value
            except ValueError as e:
                print(e)
                break
        return total

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sg = SumGenerator(data)
    result = SumGenerator.sum_generator(sg)
    print(f"Sum of elements: {result}")