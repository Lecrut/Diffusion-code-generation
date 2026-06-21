class TimeConverter:
    def __init__(self):
        self.conversion_factors = {
            'seconds_to_minutes': 1 / 60,
            'minutes_to_hours': 1 / 60,
            'hours_to_days': 1 / 24,
            'days_to_weeks': 1 / 7,
            'weeks_to_years': 1 / 52.1429
        }

    def convert(self, from_unit, to_unit, value):
        try:
            factor = self.conversion_factors[f'{from_unit}_to_{to_unit}']
            return value * factor
        except KeyError:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")

if __name__ == '__main__':
    converter = TimeConverter()
    seconds = 3600
    minutes = converter.convert('seconds', 'minutes', seconds)
    hours = converter.convert('minutes', 'hours', minutes)
    days = converter.convert('hours', 'days', hours)
    weeks = converter.convert('days', 'weeks', days)
    print(f"Seconds: {seconds}, Minutes: {minutes}, Hours: {hours}, Days: {days}, Weeks: {weeks}")