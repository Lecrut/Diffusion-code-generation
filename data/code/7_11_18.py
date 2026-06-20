class TimeConverter:
    SECONDS_PER_MINUTE = 60
    MINUTES_PER_HOUR = 60
    HOURS_PER_DAY = 24
    DAYS_PER_WEEK = 7
    DAYS_PER_MONTH = 30
    DAYS_PER_YEAR = 365

    def seconds_to_minutes(self, seconds):
        if seconds < 0:
            raise ValueError("Seconds cannot be negative")
        return seconds / self.SECONDS_PER_MINUTE

    def seconds_to_hours(self, seconds):
        if seconds < 0:
            raise ValueError("Seconds cannot be negative")
        return seconds / (self.SECONDS_PER_MINUTE * self.MINUTES_PER_HOUR)

    def seconds_to_days(self, seconds):
        if seconds < 0:
            raise ValueError("Seconds cannot be negative")
        return seconds / (self.SECONDS_PER_MINUTE * self.MINUTES_PER_HOUR * self.HOURS_PER_DAY)

    def minutes_to_seconds(self, minutes):
        if minutes < 0:
            raise ValueError("Minutes cannot be negative")
        return minutes * self.SECONDS_PER_MINUTE

    def minutes_to_hours(self, minutes):
        if minutes < 0:
            raise ValueError("Minutes cannot be negative")
        return minutes / self.MINUTES_PER_HOUR

    def minutes_to_days(self, minutes):
        if minutes < 0:
            raise ValueError("Minutes cannot be negative")
        return minutes / (self.MINUTES_PER_HOUR * self.HOURS_PER_DAY)

    def hours_to_seconds(self, hours):
        if hours < 0:
            raise ValueError("Hours cannot be negative")
        return hours * self.MINUTES_PER_HOUR * self.SECONDS_PER_MINUTE

    def hours_to_minutes(self, hours):
        if hours < 0:
            raise ValueError("Hours cannot be negative")
        return hours * self.MINUTES_PER_HOUR

    def hours_to_days(self, hours):
        if hours < 0:
            raise ValueError("Hours cannot be negative")
        return hours / self.HOURS_PER_DAY

    def days_to_seconds(self, days):
        if days < 0:
            raise ValueError("Days cannot be negative")
        return days * self.HOURS_PER_DAY * self.MINUTES_PER_HOUR * self.SECONDS_PER_MINUTE

    def days_to_hours(self, days):
        if days < 0:
            raise ValueError("Days cannot be negative")
        return days * self.HOURS_PER_DAY

    def days_to_minutes(self, days):
        if days < 0:
            raise ValueError("Days cannot be negative")
        return days * self.HOURS_PER_DAY * self.MINUTES_PER_HOUR

    def weeks_to_days(self, weeks):
        if weeks < 0:
            raise ValueError("Weeks cannot be negative")
        return weeks * self.DAYS_PER_WEEK

    def weeks_to_hours(self, weeks):
        if weeks < 0:
            raise ValueError("Weeks cannot be negative")
        return weeks * self.DAYS_PER_WEEK * self.HOURS_PER_DAY

    def weeks_to_minutes(self, weeks):
        if weeks < 0:
            raise ValueError("Weeks cannot be negative")
        return weeks * self.DAYS_PER_WEEK * self.HOURS_PER_DAY * self.MINUTES_PER_HOUR

    def weeks_to_seconds(self, weeks):
        if weeks < 0:
            raise ValueError("Weeks cannot be negative")
        return weeks * self.DAYS_PER_WEEK * self.HOURS_PER_DAY * self.MINUTES_PER_HOUR * self.SECONDS_PER_MINUTE

    def years_to_days(self, years):
        if years < 0:
            raise ValueError("Years cannot be negative")
        return years * self.DAYS_PER_YEAR

    def years_to_hours(self, years):
        if years < 0:
            raise ValueError("Years cannot be negative")
        return years * self.DAYS_PER_YEAR * self.HOURS_PER_DAY

    def years_to_minutes(self, years):
        if years < 0:
            raise ValueError("Years cannot be negative")
        return years * self.DAYS_PER_YEAR * self.HOURS_PER_DAY * self.MINUTES_PER_HOUR

    def years_to_seconds(self, years):
        if years < 0:
            raise ValueError("Years cannot be negative")
        return years * self.DAYS_PER_YEAR * self.HOURS_PER_DAY * self.MINUTES_PER_HOUR * self.SECONDS_PER_MINUTE

if __name__ == '__main__':
    converter = TimeConverter()
    sample_seconds = 3661
    print(converter.seconds_to_minutes(sample_seconds))
    print(converter.seconds_to_hours(sample_seconds))
    print(converter.seconds_to_days(sample_seconds))
    print(converter.days_to_seconds(2))
    print(converter.weeks_to_hours(1))
    print(converter.years_to_minutes(1))