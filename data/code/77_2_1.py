class TimeConverter:
    def convert_to_total_minutes(self, time_tuple):
        hours, minutes, seconds = time_tuple
        total_minutes = hours * 60 + minutes + seconds / 60
        return total_minutes
if __name__ == '__main__':
    converter = TimeConverter()
    sample_time1 = (2, 30, 0)
    sample_time2 = (1, 59, 59)
    sample_time3 = (0, 0, 120)
    result1 = converter.convert_to_total_minutes(sample_time1)
    result2 = converter.convert_to_total_minutes(sample_time2)
    result3 = converter.convert_to_total_minutes(sample_time3)
    print(f"Time {sample_time1} in total minutes: {result1}")
    print(f"Time {sample_time2} in total minutes: {result2}")
    print(f"Time {sample_time3} in total minutes: {result3}")