class TimeZoneDifferenceCalculator:
    DEFAULT_OFFSETS = [5, -3, 2.5, 0, -8]
    
    @staticmethod
    def calculate_difference(offsets):
        if not offsets:
            raise ValueError("The list of time zone offsets cannot be empty.")
        min_offset = min(offsets)
        max_offset = max(offsets)
        return max_offset - min_offset

if __name__ == '__main__':
    sample_offsets = TimeZoneDifferenceCalculator.DEFAULT_OFFSETS
    difference = TimeZoneDifferenceCalculator.calculate_difference(sample_offsets)
    print(difference)