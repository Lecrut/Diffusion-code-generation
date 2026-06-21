THIRD_INDEX = 2

class ListAccessor:
    def __init__(self, data):
        self.data = data

    def get_third(self):
        if len(self.data) <= THIRD_INDEX:
            raise IndexError("Insufficient elements in list")
        return self.data[THIRD_INDEX]

    def get_length(self):
        return len(self.data)

if __name__ == '__main__':
    sample_values = ["alpha", "bravo", "charlie", "delta", "echo"]
    accessor = ListAccessor(sample_values)
    print(accessor.get_third())
    print(accessor.get_length())