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

    def seconds_to_hours(self, seconds):
        return self.minutes_to_hours(self.seconds_to_minutes(seconds))

    def minutes_to_days(self, minutes):
        return self.hours_to_days(self.minutes_to_hours(minutes))

    def hours_to_years(self, hours):
        return self.weeks_to_years(self.days_to_weeks(self.hours_to_days(hours)))
if __name__ == '__main__':
    converter = TimeConverter()
    print(converter.seconds_to_minutes(3600))
    print(converter.minutes_to_hours(120))
    print(converter.hours_to_days(48))
    print(converter.days_to_weeks(35))
    print(converter.weeks_to_years(52))
    print(converter.seconds_to_hours(7200))
    print(converter.minutes_to_days(1440))
    print(converter.hours_to_years(8760))