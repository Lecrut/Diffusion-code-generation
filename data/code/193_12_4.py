class ListSummer:
    def __init__(self, data):
        self._data = data
    def calculate_sum(self):
        return sum(self._data)
if __name__ == '__main__':
    sample_list = [10, 25, 30, 45, 50]
    summer = ListSummer(sample_list)
    total = summer.calculate_sum()
    print(total)