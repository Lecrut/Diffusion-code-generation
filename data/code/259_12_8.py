class ValueExtremes:
    def find_min(self, numbers):
        return min(numbers)

    def find_max(self, numbers):
        return max(numbers)

if __name__ == '__main__':
    values = [3, 5, 1, 8, 2]
    value_extremes = ValueExtremes()
    print("Minimum:", value_extremes.find_min(values))
    print("Maximum:", value_extremes.find_max(values))