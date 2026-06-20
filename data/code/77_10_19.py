class TimeConverter:
    HOURS_TO_MINUTES = 60

    def convert_to_total_minutes(self, time_str):
        hours, minutes, seconds = map(int, time_str.split(':'))
        return (hours * self.HOURS_TO_MINUTES) + minutes + seconds / 60

if __name__ == '__main__':
    converter = TimeConverter()
    print(converter.convert_to_total_minutes('1:30:45'))