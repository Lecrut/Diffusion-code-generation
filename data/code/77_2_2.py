class TimeConverter:
    def convert_to_total_minutes(self, time_tuple):
        hours, minutes, seconds = time_tuple
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