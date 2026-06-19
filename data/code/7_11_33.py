class TimeConverter:

    def seconds_to_minutes(self, seconds):
        return seconds / 60

    def minutes_to_hours(self, minutes):
        return minutes / 60

    def hours_to_days(self, hours):
        return hours / 24

    def days_to_years(self, days):
        return days / 365.25
if __name__ == '__main__':
    converter = TimeConverter()
    seconds = 7200
    minutes = 180
    hours = 9
    days = 365
    print(f'{seconds} seconds is {converter.seconds_to_minutes(seconds)} minutes')
    print(f'{minutes} minutes is {converter.minutes_to_hours(minutes)} hours')
    print(f'{hours} hours is {converter.hours_to_days(hours)} days')
    print(f'{days} days is {converter.days_to_years(days)} years')