class ListOperations:
    def __init__(self, data):
        self._data = list(data)
    def get_sum(self):
        return sum(self._data)
if __name__ == '__main__':
    sample_list = [1, 5, 10, 2]
    operations = ListOperations(sample_list)
    result = operations.get_sum()
    print(result)