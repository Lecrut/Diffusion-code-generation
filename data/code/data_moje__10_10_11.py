class ElementAccess:
    def __init__(self, data):
        self.data = data

    def get_first(self):
        return self.data[0]

    def get_length(self):
        return len(self.data)

if __name__ == '__main__':
    numbers = [100, 200, 300, 400, 500]
    accessor = ElementAccess(numbers)
    print(accessor.get_first())
    print(accessor.get_length())