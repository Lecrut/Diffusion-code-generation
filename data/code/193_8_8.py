class SumGenerator:
    def __init__(self, data):
        self.data = iter(data)

    def sum_elements(self):
        total = 0
        for item in self.data:
            total += item
        return total

if __name__ == '__main__':
    sample_data = range(1, 1000001)
    sg = SumGenerator(sample_data)
    result = sg.sum_elements()
    print(f"Sum of elements: {result}")