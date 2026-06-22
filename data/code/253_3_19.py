class FindTheMiddleValueAmongThreeProcessor:
    def __init__(self):
        self.data = []

    def update(self, value):
        self.data.append(value)

    def get_middle_value(self):
        if len(self.data) == 0:
            return None
        sorted_data = sorted(self.data)
        middle_index = len(sorted_data) // 2
        return sorted_data[middle_index]

if __name__ == '__main__':
    processor = FindTheMiddleValueAmongThreeProcessor()
    processor.update(5)
    processor.update(3)
    processor.update(8)
    print(processor.get_middle_value())