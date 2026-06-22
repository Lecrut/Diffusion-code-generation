class FindTheMiddleValueAmongThreeProcessor:
    def __init__(self):
        self.data = []

    def update_data(self, value):
        if len(self.data) < 3:
            self.data.append(value)
        else:
            raise ValueError("Only three values are allowed.")

    @staticmethod
    def find_middle(values):
        return sorted(values)[1]

    def get_middle_value(self):
        if len(self.data) != 3:
            raise ValueError("Exactly three values are required to find the middle value.")
        return self.find_middle(self.data)

if __name__ == '__main__':
    processor = FindTheMiddleValueAmongThreeProcessor()
    processor.update_data(5)
    processor.update_data(2)
    processor.update_data(8)
    print(processor.get_middle_value())