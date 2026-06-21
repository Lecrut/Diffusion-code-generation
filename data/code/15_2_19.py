class ListAccessor:
    def __init__(self, data):
        self.data = data

    def get_second_last(self):
        return self.data[-2]

if __name__ == '__main__':
    sample_values = [100, 200, 300, 400, 500]
    accessor = ListAccessor(sample_values)
    result1 = accessor.get_second_last()
    result2 = len(sample_values)
    print(result1)
    print(result2)