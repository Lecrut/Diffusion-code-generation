class TimeConverter:
    def validate_time_tuple(self, time_tuple):
        if len(time_tuple) != 3:
            raise ValueError("Time tuple must contain exactly three elements")
        hours, minutes, seconds = time_tuple
        if not (isinstance(hours, int) and isinstance(minutes, int) and isinstance(seconds, int)):
            raise TypeError("All elements in the time tuple must be integers")
        if not (0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60):
            raise ValueError("Invalid time values")

    def convert_to_total_minutes(self, time_tuple):
        self.validate_time_tuple(time_tuple)
        hours, minutes, seconds = time_tuple
        total_minutes = (hours * 60) + minutes + (seconds / 60)
        return total_minutes

if __name__ == '__main__':
    converter = TimeConverter()
    sample_time1 = (1, 30, 0)
    sample_time2 = (2, 15, 30)
    sample_time3 = (0, 5, 59)
    result1 = converter.convert_to_total_minutes(sample_time1)
    result2 = converter.convert_to_total_minutes(sample_time2)
    result3 = converter.convert_to_total_minutes(sample_time3)
    print(f"Time {sample_time1} converted to total minutes: {result1}")
    print(f"Time {sample_time2} converted to total minutes: {result2}")
    print(f"Time {sample_time3} converted to total minutes: {result3}")