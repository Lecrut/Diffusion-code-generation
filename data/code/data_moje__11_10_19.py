class SequenceAccessor:
    def __init__(self, sequence):
        self.sequence = sequence

    def last_item(self):
        return self.sequence[-1]

if __name__ == '__main__':
    sample_data = [42, 7, 19, 88, 3, 2024]
    accessor = SequenceAccessor(sample_data)
    print(accessor.last_item())