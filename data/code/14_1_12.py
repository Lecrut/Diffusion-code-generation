class ArrayAccessor:
    def __init__(self, data):
        self.data = data

    def third_element(self):
        if len(self.data) > 2:
            return self.data[2]
        return None

    def size(self):
        return len(self.data)

if __name__ == '__main__':
    accessor = ArrayAccessor([1, 2, 3, 4, 5])
    print(accessor.third_element())
    print(accessor.size())
    empty_accessor = ArrayAccessor([])
    print(empty_accessor.third_element())