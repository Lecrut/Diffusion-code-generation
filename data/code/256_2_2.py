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
    data2 = [100, 50, 200, 10]
    data3 = []
    data4 = [7]
    range1 = calculator.find_range(data1)
    print(f"Range of {data1}: {range1}")
    range2 = calculator.find_range(data2)
    print(f"Range of {data2}: {range2}")
    range3 = calculator.find_range(data3)
    print(f"Range of {data3}: {range3}")
    range4 = calculator.find_range(data4)
    print(f"Range of {data4}: {range4}")