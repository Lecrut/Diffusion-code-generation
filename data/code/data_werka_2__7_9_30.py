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
    print(f'Seconds: {seconds} -> Minutes: {minutes}')
    print(f'Minutes: {minutes} -> Hours: {hours}')
    print(f'Hours: {hours} -> Days: {days}')
    print(f'Days: {days} -> Weeks: {weeks}')
    print(f'Weeks: {weeks} -> Years: {years}')
    print(f'Years: {years} -> Decades: {decades}')
    print(f'Decades: {decades} -> Centuries: {centuries}')