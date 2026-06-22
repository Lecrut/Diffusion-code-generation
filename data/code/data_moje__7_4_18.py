class TimeConverter:
    def __init__(self):
        self.seconds_per_minute = 60
        self.seconds_per_hour = 3600
        self.seconds_per_day = 86400
        self.seconds_per_week = 604800
        self.days_per_month = 30.4375
        self.seconds_per_month = 2629746.0
        self.days_per_year = 365.25
        self.seconds_per_year = 31557600.0

    def convert_to_seconds(self, value, unit):
        unit = unit.lower()
        if unit == 'seconds':
            return value
        if unit == 'minutes':
            return value * self.seconds_per_minute
        if unit == 'hours':
            return value * self.seconds_per_hour
        if unit == 'days':
            return value * self.seconds_per_day
        if unit == 'weeks':
            return value * self.seconds_per_week
        if unit == 'months':
            return value * self.seconds_per_month
        if unit == 'years':
            return value * self.seconds_per_year
        raise ValueError(f"Unknown unit: {unit}")

    def convert_from_seconds(self, seconds, unit):
        unit = unit.lower()
        if unit == 'seconds':
            return seconds
        if unit == 'minutes':
            return seconds / self.seconds_per_minute
        if unit == 'hours':
            return seconds / self.seconds_per_hour
        if unit == 'days':
            return seconds / self.seconds_per_day
        if unit == 'weeks':
            return seconds / self.seconds_per_week
        if unit == 'months':
            return seconds / self.seconds_per_month
        if unit == 'years':
            return seconds / self.seconds_per_year
        raise ValueError(f"Unknown target unit: {unit}")

    def convert(self, value, from_unit, to_unit):
        seconds = self.convert_to_seconds(value, from_unit)
        return self.convert_from_seconds(seconds, to_unit)

def run_sample():
    converter = TimeConverter()
    years = 2.5
    seconds_in_2_5_years = converter.convert_to_seconds(years, 'years')
    minutes_in_2_5_years = converter.convert(seconds_in_2_5_years, 'seconds', 'minutes')
    days_in_2_5_years = converter.convert(seconds_in_2_5_years, 'seconds', 'days')
    print(f"Seconds in {years} years: {seconds_in_2_5_years}")
    print(f"Minutes in {years} years: {minutes_in_2_5_years}")
    print(f"Days in {years} years: {days_in_2_5_years}")

if __name__ == '__main__':
    run_sample()