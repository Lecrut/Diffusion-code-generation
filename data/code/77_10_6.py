class TimeConverter:

    def convert_to_total_minutes(self, time_str):
        hours, minutes, seconds = map(int, time_str.split(':'))
        return hours * 60 + minutes + seconds / 60
if __name__ == '__main__':
    converter = TimeConverter()
    print(converter.convert_to_total_minutes('1:30:45'))
    print(converter.convert_to_total_minutes('2:00:00'))