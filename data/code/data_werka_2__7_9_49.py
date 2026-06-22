class TimeConverter:
    SECONDS_PER_MINUTE = 60
    MINUTES_PER_HOUR = 60
    HOURS_PER_DAY = 24
    DAYS_PER_WEEK = 7
    WEEKS_PER_YEAR = 52.1429
    YEARS_PER_DECADE = 10
    DECADES_PER_CENTURY = 10

    def seconds_to_minutes(self, seconds):
        return seconds / self.SECONDS_PER_MINUTE

    def minutes_to_hours(self, minutes):
        return minutes / self.MINUTES_PER_HOUR

    def hours_to_days(self, hours):
        return hours / self.HOURS_PER_DAY

    def days_to_weeks(self, days):
        return days / self.DAYS_PER_WEEK

    def weeks_to_years(self, weeks):
        return weeks / self.WEEKS_PER_YEAR

    def years_to_decades(self, years):
        return years / self.YEARS_PER_DECADE

    def decades_to_centuries(self, decades):
        return decades / self.DECADES_PER_CENTURY

    @staticmethod
    def convert_time(value, from_unit, to_unit):
        converter = TimeConverter()
        conversion_path = {
            'seconds': ['minutes', 'hours', 'days', 'weeks', 'years'],
            'minutes': ['hours', 'days', 'weeks', 'years'],
            'hours': ['days', 'weeks', 'years'],
            'days': ['weeks', 'years'],
            'weeks': ['years'],
            'years': []
        }

        if from_unit not in conversion_path or to_unit not in conversion_path:
            raise ValueError("Unsupported time unit")

        path = conversion_path[from_unit]
        current_value = value

        for step in range(len(path)):
            method_name = f"{path[step]}_to_{path[step + 1] if step < len(path) - 1 else to_unit}"
            method = getattr(converter, method_name)
            current_value = method(current_value)

        return current_value

if __name__ == '__main__':
    converter = TimeConverter()
    seconds = 3600
    minutes = converter.seconds_to_minutes(seconds)
    hours = converter.minutes_to_hours(minutes)
    days = converter.hours_to_days(hours)
    weeks = converter.days_to_weeks(days)
    years = converter.weeks_to_years(weeks)

    print(f"Seconds: {seconds} -> Minutes: {minutes}")
    print(f"Minutes: {minutes} -> Hours: {hours}")
    print(f"Hours: {hours} -> Days: {days}")
    print(f"Days: {days} -> Weeks: {weeks}")
    print(f"Weeks: {weeks} -> Years: {years}")

    direct_conversion = converter.convert_time(seconds, 'seconds', 'years')
    print(f"Direct conversion from seconds to years: {direct_conversion}")