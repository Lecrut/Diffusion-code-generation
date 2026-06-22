class ValueExtremes:
    def find_min(self, numbers):
        return min(numbers)

    def find_max(self, numbers):
        return max(numbers)

if __name__ == '__main__':
    values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    extremes = ValueExtremes()
    print("Minimum:", extremes.find_min(values))
    print("Maximum:", extremes.find_max(values))