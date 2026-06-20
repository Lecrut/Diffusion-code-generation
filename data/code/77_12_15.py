class TimeConverter:
    @staticmethod
    def convert_to_total_minutes(time_str: str) -> int:
        hours, minutes = map(int, time_str.split(':'))
        total_minutes = hours * 60 + minutes
        return total_minutes

if __name__ == '__main__':
    converter = TimeConverter()
    time1 = "01:30"
    result1 = converter.convert_to_total_minutes(time1)
    print(f"Time: {time1}, Total Minutes: {result1}")

    time2 = "23:59"
    result2 = converter.convert_to_total_minutes(time2)
    print(f"Time: {time2}, Total Minutes: {result2}")