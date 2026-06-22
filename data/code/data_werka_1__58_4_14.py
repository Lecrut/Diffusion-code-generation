class ListManager:
    def __init__(self, data):
        self.data = data

    @classmethod
    def from_csv_string(cls, csv_string):
        return cls(csv_string.split(','))

    def validate_data(self):
        if not isinstance(self.data, list) or len(self.data) == 0:
            raise ValueError("Data must be a non-empty list")

    def get_first_element(self):
        self.validate_data()
        return self.data[0]

if __name__ == '__main__':
    sample_list = [100, 200, 300, 400]
    manager = ListManager(sample_list)
    first_element = manager.get_first_element()
    print(first_element)

    csv_string = "alpha,beta,gamma"
    csv_manager = ListManager.from_csv_string(csv_string)
    first_csv_element = csv_manager.get_first_element()
    print(first_csv_element)