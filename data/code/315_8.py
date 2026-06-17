class Sequence:
    def __init__(self, elements):
        self.elements = elements
    def generate_infinite_pattern(self):
        cycle_length = len(self.elements)
        if cycle_length == 0:
            return []
        result = []
        while True:
            for i, element in enumerate(self.elements):
                result.append(element)
            if result:
                yield from result
            if len(result) > 1000000:
                break
if __name__ == '__main__':
    sample_elements = [1, 2, 3, 4]
    seq = Sequence(sample_elements)
    print("Generating first 20 elements:")
    for i in range(20):
        print(next(seq.generate_infinite_pattern()))
    print("\nGenerating next 10 elements (to show repetition):")
    for i in range(10):
        print(next(seq.generate_infinite_pattern()))