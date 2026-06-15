class ListSummer:
    def __init__(self, data):
        self._data = data
    def sum_elements(self):
        return sum(self._data)
if __name__ == '__main__':
    sample_list = [1, 5, 10, 2]
    summer = ListSummer(sample_list)
    result = summer.sum_elements()
    print(result)