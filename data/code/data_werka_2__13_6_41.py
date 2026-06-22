class TimeZoneDifferenceCalculator:
    def __init__(self, offsets):
        if not offsets:
            raise ValueError("The list of time zone offsets cannot be empty.")
        self.offsets = offsets

    def find_min_offset(self):
        return min(self.offsets)

    def find_max_offset(self):
        return max(self.offsets)

    def compute_difference(self):
        return self.find_max_offset() - self.find_min_offset()

if __name__ == '__main__':
    sample_offsets = [10, -5, 4.5, 1, -9]
    calculator = TimeZoneDifferenceCalculator(sample_offsets)
    min_offset = calculator.find_min_offset()
    max_offset = calculator.find_max_offset()
    difference = calculator.compute_difference()
    
    print(f"Minimum Offset: {min_offset}")
    print(f"Maximum Offset: {max_offset}")
    print(f"Difference: {difference}")