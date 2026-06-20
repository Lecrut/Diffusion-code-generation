class TimeConverter:
    def convert_to_total_minutes(self, time_tuple):
        hours, minutes, seconds = time_tuple
        if not (isinstance(hours, int) and isinstance(minutes, int) and isinstance(seconds, int)):
            raise ValueError("All elements of the time tuple must be integers.")
        if hours < 0 or minutes < 0 or seconds < 0:
            raise ValueError("Hours, minutes, and seconds must be non-negative.")
        if seconds >= 60:
            raise ValueError("Seconds must be less than 60.")
        total_minutes = hours * 60 + minutes + seconds / 60
        return total_minutes

if __name__ == '__main__':
    converter = TimeConverter()
    sample_time1 = (1, 30, 0)
    sample_time2 = (2, 15, 45)
    sample_time3 = (0, 5, 30)
    result1 = converter.convert_to_total_minutes(sample_time1)
    result2 = converter.convert_to_total_minutes(sample_time2)
    result3 = converter.convert_to_total_minutes(sample_time3)
    print(f"Time {sample_time1} converted to total minutes: {result1}")
    print(f"Time {sample_time2} converted to total minutes: {result2}")
    print(f"Time {sample_time3} converted to total minutes: {result3}")