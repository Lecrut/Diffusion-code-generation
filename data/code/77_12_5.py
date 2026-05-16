class TimeConverter:
    def convert_to_total_minutes(self, time_str: str) -> int:
        parts = time_str.split(':')
        if len(parts) != 3:
            raise ValueError("Invalid time format. Expected HH:MM:SS")
        try:
            hours = int(parts[0])
            minutes = int(parts[1])
            seconds = int(parts[2])
        except ValueError:
            raise ValueError("Time components must be integers")
        total_minutes = hours * 60 + minutes + seconds / 60
        total_seconds = hours * 3600 + minutes * 60 + seconds
        return total_seconds // 60
if __name__ == '__main__':
    converter = TimeConverter()
    time1 = "01:30:00"
    result1 = converter.convert_to_total_minutes(time1)
    print(f"Time: {time1}, Total Minutes: {result1}")
    time2 = "00:05:30"
    result2 = converter.convert_to_total_minutes(time2)
    print(f"Time: {time2}, Total Minutes: {result2}")
    time3 = "23:59:59"
    result3 = converter.convert_to_total_minutes(time3)
    print(f"Time: {time3}, Total Minutes: {result3}")
    time4 = "00:00:00"
    result4 = converter.convert_to_total_minutes(time4)
    print(f"Time: {time4}, Total Minutes: {result4}")