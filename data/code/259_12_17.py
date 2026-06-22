class ValueExtremes:
    def find_min(self, numbers):
        return min(numbers)

    def find_max(self, numbers):
        return max(numbers)

if __name__ == '__main__':
    values = [34, 78, 12, 56, 90, 23]
    ve = ValueExtremes()
    print("Minimum:", ve.find_min(values))
    print("Maximum:", ve.find_max(values))