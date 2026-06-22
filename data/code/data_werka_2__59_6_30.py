class MiddleElementGenerator:
    def __init__(self, sequence):
        self.sequence = sequence

    def generate(self):
        length = len(self.sequence)
        if length == 0:
            raise ValueError("The sequence is empty")
        
        mid_index = length // 2
        if length % 2 == 1:
            yield self.sequence[mid_index]
        else:
            yield self.sequence[mid_index - 1]
            yield self.sequence[mid_index]

if __name__ == '__main__':
    sample_sequence_odd = [1, 2, 3, 4, 5]
    sample_sequence_even = [1, 2, 3, 4, 5, 6]

    print("Middle elements of odd-length sequence:")
    generator_odd = MiddleElementGenerator(sample_sequence_odd)
    try:
        for middle in generator_odd.generate():
            print(middle)
    except ValueError as e:
        print(e)

    print("\nMiddle elements of even-length sequence:")
    generator_even = MiddleElementGenerator(sample_sequence_even)
    try:
        for middle in generator_even.generate():
            print(middle)
    except ValueError as e:
        print(e)