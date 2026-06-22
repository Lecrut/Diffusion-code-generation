class TimeConverter:

    def seconds_to_minutes(self, seconds):
        return seconds / 60

    def minutes_to_hours(self, minutes):
        return minutes / 60

    def hours_to_days(self, hours):
        return hours / 24

    def days_to_weeks(self, days):
        return days / 7

    def weeks_to_years(self, weeks):
        return weeks / 52.1429

    def years_to_decades(self, years):
        return years / 10

    def decades_to_centuries(self, decades):
        return decades / 10
if __name__ == '__main__':
    converter = TimeConverter()
    seconds = 3600
    minutes = converter.seconds_to_minutes(seconds)
    hours = converter.minutes_to_hours(minutes)
    days = converter.hours_to_days(hours)
    weeks = converter.days_to_weeks(days)
    years = converter.weeks_to_years(weeks)
    decades = converter.years_to_decades(years)
    centuries = converter.decades_to_centuries(decades)
    print(f'{seconds} seconds is {minutes} minutes')
    print(f'{minutes} minutes is {hours} hours')
    print(f'{hours} hours is {days} days')
    print(f'{days} days is {weeks} weeks')
    print(f'{weeks} weeks is {years} years')
    print(f'{years} years is {decades} decades')
    print(f'{decades} decades is {centuries} centuries')