class MinFinder:
    @staticmethod
    def filter_negatives(values):
        return [value for value in values if value >= 0]

    @staticmethod
    def find_minimum(filtered_values):
        return min(filtered_values) if filtered_values else None

    @classmethod
    def find_min_with_negatives(cls, values):
        negative_filtered = cls.filter_negatives(values)
        return cls.find_minimum(negative_filtered)

if __name__ == '__main__':
    data1 = [5, 2, -8, 1, 9]
    result1 = MinFinder.find_min_with_negatives(data1)
    print(f"Data: {data1}, Minimum (non-negative): {result1}")

    data2 = [-10, -5, -20, -1]
    result2 = MinFinder.find_min_with_negatives(data2)
    print(f"Data: {data2}, Minimum (non-negative): {result2}")

    data3 = [100, 50, 25, 75, -30]
    result3 = MinFinder.find_min_with_negatives(data3)
    print(f"Data: {data3}, Minimum (non-negative): {result3}")