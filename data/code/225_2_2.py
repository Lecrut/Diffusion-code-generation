class MinMaxFinder:
    def calculate_range(self, numbers):
        if not numbers:
            return None, None, None
        minimum = min(numbers)
        maximum = max(numbers)
        range_value = maximum - minimum
        return minimum, maximum, range_value
if __name__ == '__main__':
    finder = MinMaxFinder()
    data1 = [1.5, 3.14, 2.71, 0.99, 5.0]
    min1, max1, range1 = finder.calculate_range(data1)
    print(f"Data: {data1}")
    print(f"Minimum: {min1}")
    print(f"Maximum: {max1}")
    print(f"Range: {range1}")
    data2 = [-10.5, 0.0, 5.5, -3.2]
    min2, max2, range2 = finder.calculate_range(data2)
    print(f"\nData: {data2}")
    print(f"Minimum: {min2}")
    print(f"Maximum: {max2}")
    print(f"Range: {range2}")
    data3 = [42.0]
    min3, max3, range3 = finder.calculate_range(data3)
    print(f"\nData: {data3}")
    print(f"Minimum: {min3}")
    print(f"Maximum: {max3}")
    print(f"Range: {range3}")
    data4 = []
    min4, max4, range4 = finder.calculate_range(data4)
    print(f"\nData: {data4}")
    print(f"Minimum: {min4}")
    print(f"Maximum: {max4}")
    print(f"Range: {range4}")