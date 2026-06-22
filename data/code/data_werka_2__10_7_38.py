class TemperatureComparison:
    def __init__(self, tolerance=1):
        self.tolerance = tolerance

    def set_tolerance(self, new_tolerance):
        if not isinstance(new_tolerance, (int, float)) or new_tolerance < 0:
            raise ValueError("Tolerance must be a non-negative number.")
        self.tolerance = new_tolerance

    def compare(self, temp1, temp2):
        if not all(isinstance(temp, (int, float)) for temp in [temp1, temp2]):
            raise ValueError("Both temperature values must be numbers.")
        return abs(temp1 - temp2) <= self.tolerance

if __name__ == '__main__':
    try:
        comparator = TemperatureComparison()
        sample_temp1 = 27.0
        sample_temp2 = 28.0
        result_within_tolerance = comparator.compare(sample_temp1, sample_temp2)
        print("Are temperatures within tolerance?", result_within_tolerance)

        comparator.set_tolerance(2)
        result_with_new_tolerance = comparator.compare(sample_temp1, sample_temp2)
        print("Are temperatures within new tolerance?", result_with_new_tolerance)

    except ValueError as e:
        print(e)