class ValueExtremes:
    def find_min(self, numbers):
        return min(numbers)

    def find_max(self, numbers):
        return max(numbers)

if __name__ == '__main__':
    values = [34, 78, 12, 56, 90]
    extremes = ValueExtremes()
    print("Minimum:", extremes.find_min(values))
    print("Maximum:", extremes.find_max(values))