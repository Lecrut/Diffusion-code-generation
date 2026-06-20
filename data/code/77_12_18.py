class TimeConverter:
    def convert_to_total_minutes(self, time_str: str) -> int:
        hours = int(time_str[:2])
        minutes = int(time_str[3:5])
        return hours * 60 + minutes

if __name__ == '__main__':
    converter = TimeConverter()
    time1 = "01:30"
    result1 = converter.convert_to_total_minutes(time1)
    print(f"Time: {time1}, Total Minutes: {result1}")
    
    time2 = "23:59"
    result2 = converter.convert_to_total_minutes(time2)
    print(f"Time: {time2}, Total Minutes: {result2}")