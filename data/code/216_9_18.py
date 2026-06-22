class MedianCalculator:
    @staticmethod
    def calculate_middle(data):
        n = len(data)
        middle_index = n // 2
        return data[middle_index]

if __name__ == '__main__':
    calculator = MedianCalculator()
    sorted_list = [1, 5, 8, 12, 16]
    middle_value = calculator.calculate_middle(sorted_list)
    print(middle_value)