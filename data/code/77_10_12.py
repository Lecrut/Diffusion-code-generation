class TimeConverter:
    def convert_to_total_minutes(self, time_str):
        hours, minutes, seconds = map(int, time_str.split(':'))
        total_minutes = hours * 60 + minutes + (seconds // 60)
        return total_minutes

if __name__ == '__main__':
    converter = TimeConverter()
    sample_time = "02:45:30"
    result = converter.convert_to_total_minutes(sample_time)
    print(result)