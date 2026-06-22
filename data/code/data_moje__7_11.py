class TimeConverter:
    def __init__(self):
        self.base_unit = 'seconds'
        self.conversion_factors = {
            'seconds': 1,
            'minutes': 60,
            'hours': 3600,
            'days': 86400,
            'weeks': 604800,
            'months': 2592000,
            'years': 31536000
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.conversion_factors:
            raise ValueError(f"Unsupported unit: {from_unit}")
        if to_unit not in self.conversion_factors:
            raise ValueError(f"Unsupported unit: {to_unit}")
        
        base_value = value * self.conversion_factors[from_unit]
        result = base_value / self.conversion_factors[to_unit]
        return result

    def seconds_to_minutes(self, seconds):
        return self.convert(seconds, 'seconds', 'minutes')

    def minutes_to_hours(self, minutes):
        return self.convert(minutes, 'minutes', 'hours')

    def hours_to_days(self, hours):
        return self.convert(hours, 'hours', 'days')

    def days_to_weeks(self, days):
        return self.convert(days, 'days', 'weeks')

    def weeks_to_years(self, weeks):
        return self.convert(weeks, 'weeks', 'years')

    def years_to_days(self, years):
        return self.convert(years, 'years', 'days')

    def custom_convert(self, value, from_unit, to_unit):
        return self.convert(value, from_unit, to_unit)

if __name__ == '__main__':
    converter = TimeConverter()
    
    print(converter.seconds_to_minutes(120))
    print(converter.minutes_to_hours(90))
    print(converter.hours_to_days(48))
    print(converter.days_to_weeks(14))
    print(converter.weeks_to_years(52))
    print(converter.years_to_days(2))
    print(converter.custom_convert(7200, 'seconds', 'hours'))
    print(converter.custom_convert(10, 'days', 'hours'))
    print(converter.custom_convert(1.5, 'years', 'months'))