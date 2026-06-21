class ArrayAccessor:
    def __init__(self, data):
        self.data = data

    def get_third_negative(self):
        return self.data[-3]

    def get_length(self):
        return len(self.data)

if __name__ == '__main__':
    accessor = ArrayAccessor([1, 2, 3, 4, 5])
    print(accessor.get_third_negative())
    print(accessor.get_length())