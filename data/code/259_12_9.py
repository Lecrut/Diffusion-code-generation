class ValueExtremes:
    def find_min(self, numbers):
        return min(numbers)

    def find_max(self, numbers):
        return max(numbers)

if __name__ == '__main__':
    ve = ValueExtremes()
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print("Minimum:", ve.find_min(sample_values))
    print("Maximum:", ve.find_max(sample_values))