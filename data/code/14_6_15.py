class SequenceAccess:
    def __init__(self, data):
        self.data = list(data)
        if len(self.data) < 3:
            raise ValueError("Sequence must contain at least three elements")

    def get_third_from_end(self):
        try:
            return self.data[-3]
        except IndexError:
            raise IndexError("Failed to access element at index -3")

if __name__ == '__main__':
    values = [5, 10, 15, 20, 25]
    accessor = SequenceAccess(values)
    print(accessor.get_third_from_end())