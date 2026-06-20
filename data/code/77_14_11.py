class TimeConverter:
    def __init__(self, time_str):
        if not isinstance(time_str, str) or len(time_str) != 5 or time_str[2] != ':':
            raise ValueError('Invalid time format')
        hours, minutes = map(int, time_str.split(':'))
        if hours < 0 or hours > 23 or minutes < 0 or (minutes > 59):
            raise ValueError('Invalid time range')
        self.hours = hours
        self.minutes = minutes

    def total_minutes(self):
        return self.hours * 60 + self.minutes

if __name__ == '__main__':
    converter = TimeConverter('1:30')
    print(converter.total_minutes())