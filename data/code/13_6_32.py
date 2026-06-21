class TimeZoneCalculator:
    def __init__(self, offsets):
        if not offsets:
            raise ValueError("The list of time zone offsets cannot be empty.")
        self.offsets = offsets

    def get_min_offset(self):
        return min(self.offsets)

    def get_max_offset(self):
        return max(self.offsets)

    def calculate_difference(self):
        return self.get_max_offset() - self.get_min_offset()

if __name__ == '__main__':
    sample_offsets = [-10, 3, 7.5, -2, 8]
    calculator = TimeZoneCalculator(sample_offsets)
    difference = calculator.calculate_difference()
    print(difference)