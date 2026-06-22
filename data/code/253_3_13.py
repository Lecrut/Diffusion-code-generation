class FindTheMiddleValueAmongThreeProcessor:
    def __init__(self):
        self.data = []

    def update_data(self, value):
        self.data.append(value)

    def get_middle_value(self):
        if len(self.data) != 3:
            raise ValueError("Exactly three values must be provided.")
        return sorted(self.data)[1]

if __name__ == '__main__':
    processor = FindTheMiddleValueAmongThreeProcessor()
    processor.update_data(5)
    processor.update_data(2)
    processor.update_data(8)
    print(processor.get_middle_value())