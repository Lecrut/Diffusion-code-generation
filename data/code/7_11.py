class TimeConverter:
    def to_minutes(self, seconds):
        return seconds / 60.0
    def to_hours(self, seconds):
        return seconds / 3600.0
    def to_days(self, seconds):
        return seconds / (60 * 60 * 24)
    def to_hours_from_days(self, days):
        return days * 24.0
if __name__ == '__main__':
    converter = TimeConverter()
    sample_seconds = 7200
    sample_minutes = 120
    sample_hours = 24
    sample_days = 3.5
    print(f"Converting {sample_seconds} seconds:")
    print(f"To minutes: {converter.to_minutes(sample_seconds)}")
    print(f"To hours: {converter.to_hours(sample_seconds)}")
    print(f"To days: {converter.to_days(sample_seconds)}")
    print("\nConverting {sample_minutes} minutes:")
    print(f"To seconds: {60 * sample_minutes}")
    print("\nConverting {sample_hours} hours:")
    print(f"To days: {converter.to_days(sample_hours * 3600)}")
    print(f"From days: {converter.to_hours_from_days(sample_days)}")