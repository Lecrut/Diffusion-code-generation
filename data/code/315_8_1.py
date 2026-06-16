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
            yield from self.elements
if __name__ == '__main__':
    sample_elements = [1, 2, 3, 4]
    seq = Sequence(sample_elements)
    print("Generating first 16 elements:")
    for i in range(16):
        pass
class Sequence:
    def __init__(self, elements):
        self.elements = elements
    def generate_infinite_pattern(self):
        cycle_length = len(self.elements)
        if cycle_length == 0:
            return
        while True:
            yield from self.elements
if __name__ == '__main__':
    sample_elements = [10, 20, 30]
    seq = Sequence(sample_elements)
    print("Generating first 9 elements:")
    count = 0
    for item in seq.generate_infinite_pattern():
        print(item, end=" ")
        count += 1
        if count >= 9:
            break
    print("\n")
    print("Generating next 7 elements (total 16):")
    for i in range(9, 16):
        item = next(seq.generate_infinite_pattern())
        print(item, end=" ")
    print("\n")