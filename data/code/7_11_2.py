class TimeConverter:
    def __init__(self):
        pass
    def seconds_to_minutes(self, seconds):
        return seconds / 60.0
    def minutes_to_seconds(self, minutes):
        return minutes * 60.0
    def minutes_to_hours(self, minutes):
        return minutes / 60.0
    def hours_to_minutes(self, hours):
        return hours * 60.0
    def hours_to_days(self, hours):
        return hours / 24.0
    def days_to_hours(self, days):
        return days * 24.0
if __name__ == '__main__':
    converter = TimeConverter()
    print("--- Seconds to Minutes ---")
    seconds_val = 120
    minutes_val = converter.seconds_to_minutes(seconds_val)
    print(f"{seconds_val} seconds is {minutes_val} minutes")
    print("\n--- Minutes to Seconds ---")
    minutes_val = 150
    seconds_val = converter.minutes_to_seconds(minutes_val)
    print(f"{minutes_val} minutes is {seconds_val} seconds")
    print("\n--- Minutes to Hours ---")
    minutes_val = 180
    hours_val = converter.minutes_to_hours(minutes_val)
    print(f"{minutes_val} minutes is {hours_val} hours")
    print("\n--- Hours to Minutes ---")
    hours_val = 5.5
    minutes_val = converter.hours_to_minutes(hours_val)
    print(f"{hours_val} hours is {minutes_val} minutes")
    print("\n--- Hours to Days ---")
    hours_val = 48
    days_val = converter.hours_to_days(hours_val)
    print(f"{hours_val} hours is {days_val} days")
    print("\n--- Days to Hours ---")
    days_val = 2.5
    hours_val = converter.days_to_hours(days_val)
    print(f"{days_val} days is {hours_val} hours")