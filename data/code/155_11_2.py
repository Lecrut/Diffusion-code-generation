class ListOperations:
    def __init__(self, data):
        self._data = data
    def get_sum(self):
        return sum(self._data)
if __name__ == '__main__':
    sample_list = [1, 5, 10, 2]
    list_ops = ListOperations(sample_list)
    result = list_ops.get_sum()
    print(result)