class FindTheMiddleValueAmongThreeProcessor:
    def __init__(self):
        self.data = []

    def update_data(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Data must be a number.")
        self.data.append(value)

    def get_middle_value(self):
        if len(self.data) != 3:
            raise ValueError("Exactly three values are required to find the middle value.")
        sorted_data = sorted(self.data)
        return sorted_data[1]

if __name__ == '__main__':
    processor = FindTheMiddleValueAmongThreeProcessor()
    processor.update_data(5)
    processor.update_data(2)
    processor.update_data(8)
    print(processor.get_middle_value())