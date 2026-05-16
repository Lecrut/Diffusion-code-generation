class TimeConverter:
    def convert_to_total_minutes(self, time_str: str) -> int:
        parts = time_str.split(':')
        if len(parts) != 3:
            raise ValueError("Invalid time format. Expected HH:MM:SS")
        h = int(parts[0])
        m = int(parts[1])
        s = int(parts[2])
        total_minutes = h * 60 + m + int(s / 60)
        return total_minutes
if __name__ == '__main__':
    converter = TimeConverter()
    time1 = "01:30:00"
    minutes1 = converter.convert_to_total_minutes(time1)
    print(f"Time: {time1}, Total Minutes: {minutes1}")
    time2 = "23:59:59"
    minutes2 = converter.convert_to_total_minutes(time2)
    print(f"Time: {time2}, Total Minutes: {minutes2}")
    time3 = "00:00:00"
    minutes3 = converter.convert_to_total_minutes(time3)
    print(f"Time: {time3}, Total Minutes: {minutes3}")
    time4 = "12:05:30"
    minutes4 = converter.convert_to_total_minutes(time4)
    print(f"Time: {time4}, Total Minutes: {minutes4}")