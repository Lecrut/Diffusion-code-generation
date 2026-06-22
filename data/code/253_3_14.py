class FindTheMiddleValueAmongThreeProcessor:
    def __init__(self):
        self.data = []

    def update_data(self, value):
        self.data.append(value)

    def get_middle_value(self):
        if len(self.data) == 0:
            return None
        sorted_data = sorted(self.data)
        middle_index = len(sorted_data) // 2
        return sorted_data[middle_index]

if __name__ == '__main__':
    processor = FindTheMiddleValueAmongThreeProcessor()
    processor.update_data(5)
    processor.update_data(3)
    processor.update_data(8)
    print(processor.get_middle_value())