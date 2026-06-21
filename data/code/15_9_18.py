class PenultimateAccessor:
    def __init__(self, data):
        self.data = data

    def get_penultimate(self):
        if not isinstance(self.data, list):
            raise TypeError("Input must be a list")
        if len(self.data) < 2:
            raise ValueError("List must have at least two elements")
        return self.data[-2]

    def get_last(self):
        if not isinstance(self.data, list):
            raise TypeError("Input must be a list")
        if len(self.data) < 1:
            raise ValueError("List must have at least one element")
        return self.data[-1]

if __name__ == '__main__':
    sample_list = [10, 25, 36, 42, 58]
    accessor = PenultimateAccessor(sample_list)
    print(accessor.get_penultimate())
    print(accessor.get_last())