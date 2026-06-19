class TimeConverter:
    def __init__(self):
        self.seconds_per_minute = 60
        self.minutes_per_hour = 60
        self.hours_per_day = 24

    def seconds_to_minutes(self, seconds):
        return seconds / self.seconds_per_minute

    def minutes_to_hours(self, minutes):
        return minutes / self.minutes_per_hour

    def hours_to_days(self, hours):
        return hours / self.hours_per_day

    def days_to_hours(self, days):
        return days * self.hours_per_day

    def hours_to_seconds(self, hours):
        return hours * self.minutes_per_hour * self.seconds_per_minute

    def minutes_to_seconds(self, minutes):
        return minutes * self.seconds_per_minute

    def days_to_minutes(self, days):
        return days * self.hours_per_day * self.minutes_per_hour

if __name__ == '__main__':
    converter = TimeConverter()
    
    seconds = 3600
    print(f"{seconds} seconds is {converter.seconds_to_minutes(seconds)} minutes")
    
    minutes = 120
    print(f"{minutes} minutes is {converter.minutes_to_hours(minutes)} hours")
    
    hours = 8
    print(f"{hours} hours is {converter.hours_to_days(hours)} days")
    
    days = 2
    print(f"{days} days is {converter.days_to_hours(days)} hours")
    
    hours = 4
    print(f"{hours} hours is {converter.hours_to_seconds(hours)} seconds")
    
    minutes = 30
    print(f"{minutes} minutes is {converter.minutes_to_seconds(minutes)} seconds")
    
    days = 1
    print(f"{days} day is {converter.days_to_minutes(days)} minutes")