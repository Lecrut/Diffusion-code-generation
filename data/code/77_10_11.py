class TimeConverter:
    SECONDS_PER_MINUTE = 60

    def convert_to_total_minutes(self, time_str):
        hours, minutes, seconds = map(int, time_str.split(':'))
        total_minutes = (hours * self.SECONDS_PER_MINUTE) + minutes + (seconds / self.SECONDS_PER_MINUTE)
        return int(total_minutes)

if __name__ == '__main__':
    converter = TimeConverter()
    print(converter.convert_to_total_minutes('01:30:45'))