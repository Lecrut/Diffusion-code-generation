class DataContainer:
    def __init__(self, data):
        self.data = data
    def find_maximum(self):
        if not self.data:
            raise ValueError("Data list is empty")
        return max(self.data)
if __name__ == '__main__':
    sample_list = [10, 5, 40, 22, 8]
    container = DataContainer(sample_list)
    maximum_value = container.find_maximum()
    print(maximum_value)