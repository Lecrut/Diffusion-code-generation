class DataContainer:
    def __init__(self, data):
        self.data = data
    def find_maximum(self):
        if not self.data:
            raise ValueError("Data list cannot be empty")
        return max(self.data)
if __name__ == '__main__':
    sample_list = [10, 4, 25, 8, 30]
    container = DataContainer(sample_list)
    maximum = container.find_maximum()
    print(maximum)