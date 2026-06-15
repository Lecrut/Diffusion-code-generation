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
    data1 = [1, 5, 2, 8, 3]
    result1 = calculator.find_range(data1)
    print(f"Range of {data1}: {result1}")
    data2 = [10, 4, 1, 9, 3]
    result2 = calculator.find_range(data2)
    print(f"Range of {data2}: {result2}")
    data3 = [5]
    result3 = calculator.find_range(data3)
    print(f"Range of {data3}: {result3}")
    data4 = []
    result4 = calculator.find_range(data4)
    print(f"Range of {data4}: {result4}")