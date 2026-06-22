class TimeConverter:
    CONVERSIONS = {
        'seconds_to_minutes': 1/60,
        'minutes_to_hours': 1/60,
        'hours_to_days': 1/24,
        'days_to_weeks': 1/7,
        'weeks_to_years': 1/52.1429
    }

    def convert(self, unit, value):
        if unit not in self.CONVERSIONS:
            raise ValueError(f"Unsupported conversion unit: {unit}")
        return value * self.CONVERSIONS[unit]

if __name__ == '__main__':
    converter = TimeConverter()
    seconds = 3600
    minutes = converter.convert('seconds_to_minutes', seconds)
    hours = converter.convert('minutes_to_hours', minutes)
    days = converter.convert('hours_to_days', hours)
    weeks = converter.convert('days_to_weeks', days)
    
    print(f"Seconds: {seconds}")
    print(f"Minutes: {minutes}")
    print(f"Hours: {hours}")
    print(f"Days: {days}")
    print(f"Weeks: {weeks}")