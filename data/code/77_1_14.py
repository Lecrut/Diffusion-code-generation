class TimeConverter:
    MINUTES_PER_HOUR = 60
    SECONDS_TO_MINUTES = 1 / 60

    @staticmethod
    def time_to_minutes(time_str):
        h, m, s = map(int, time_str.split(':'))
        total_minutes = h * TimeConverter.MINUTES_PER_HOUR + m + s * TimeConverter.SECONDS_TO_MINUTES
        return total_minutes

if __name__ == '__main__':
    converter = TimeConverter()
    sample_time1 = "01:30:00"
    result1 = converter.time_to_minutes(sample_time1)
    print(f"Time: {sample_time1}, Minutes: {result1}")
    
    sample_time2 = "00:05:30"
    result2 = converter.time_to_minutes(sample_time2)
    print(f"Time: {sample_time2}, Minutes: {result2}")
    
    sample_time3 = "23:59:59"
    result3 = converter.time_to_minutes(sample_time3)
    print(f"Time: {sample_time3}, Minutes: {result3}")