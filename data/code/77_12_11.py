class TimeConverter:
    MINUTES_PER_HOUR = 60

    @staticmethod
    def convert_to_total_minutes(time_str: str) -> int:
        parts = time_str.split(':')
        if len(parts) != 2:
            raise ValueError("Invalid time format. Expected HH:MM")
        hours = int(parts[0])
        minutes = int(parts[1])
        total_minutes = hours * TimeConverter.MINUTES_PER_HOUR + minutes
        return total_minutes

if __name__ == '__main__':
    converter = TimeConverter()
    time1 = "01:30"
    result1 = converter.convert_to_total_minutes(time1)
    print(f"Time: {time1}, Total Minutes: {result1}")

    time2 = "23:59"
    result2 = converter.convert_to_total_minutes(time2)
    print(f"Time: {time2}, Total Minutes: {result2}")