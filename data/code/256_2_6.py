class RangeCalculator:
    def find_range(self, data):
        if not data:
            return None
        minimum = data[0]
        maximum = data[0]
        for number in data:
            if number < minimum:
                minimum = number
            if number > maximum:
                maximum = number
        return maximum - minimum
if __name__ == '__main__':
    calculator = RangeCalculator()
    sample_data1 = [1, 5, 2, 8, 3]
    result1 = calculator.find_range(sample_data1)
    print(f"Range of {sample_data1}: {result1}")
    sample_data2 = [10, 4, 1, 9, 5]
    result2 = calculator.find_range(sample_data2)
    print(f"Range of {sample_data2}: {result2}")
    sample_data3 = [7]
    result3 = calculator.find_range(sample_data3)
    print(f"Range of {sample_data3}: {result3}")
    sample_data4 = []
    result4 = calculator.find_range(sample_data4)
    print(f"Range of {sample_data4}: {result4}")