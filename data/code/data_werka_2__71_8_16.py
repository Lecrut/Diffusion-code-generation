class MiddleList:
    def __init__(self, data):
        self.data = list(data)
        self.length = len(self.data)
        self._middle_index = self.length // 2
        self._middle_value = self.data[self._middle_index] if self.length > 0 else None

    def get_middle(self):
        return self._middle_value

if __name__ == '__main__':
    sample_list = MiddleList([10, 20, 30, 40, 50])
    result = sample_list.get_middle()
    print(result)