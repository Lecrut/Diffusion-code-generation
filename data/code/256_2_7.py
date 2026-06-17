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
    print(f"Data: {data1}, Range: {result1}")
    data2 = [10, 20, 5, 30]
    result2 = calculator.find_range(data2)
    print(f"Data: {data2}, Range: {result2}")
    data3 = [7]
    result3 = calculator.find_range(data3)
    print(f"Data: {data3}, Range: {result3}")
    data4 = []
    result4 = calculator.find_range(data4)
    print(f"Data: {data4}, Range: {result4}")