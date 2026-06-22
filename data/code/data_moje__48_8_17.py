class DataManager:
    def __init__(self):
        self.data = [3.14, 2.71, 1.41, 9.81, 0.57]

    def get_largest(self):
        if not self.data:
            return None
        largest = self.data[0]
        for value in self.data[1:]:
            if value > largest:
                largest = value
        return largest

if __name__ == '__main__':
    manager = DataManager()
    result = manager.get_largest()
    print(result)