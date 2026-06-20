from datetime import datetime

class TimeDifferenceCalculator:
    @staticmethod
    def calculate_duration(date1_str, date2_str):
        date_format = '%Y-%m-%d %H:%M:%S'
        date1 = datetime.strptime(date1_str, date_format)
        date2 = datetime.strptime(date2_str, date_format)
        duration = abs(date2 - date1)
        return duration.total_seconds()

    @staticmethod
    def format_duration(seconds):
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        seconds = int(seconds % 60)
        parts = []
        if hours > 0:
            parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
        if minutes > 0:
            parts.append(f"{minutes} minute{'s' if minutes != 1 else ''}")
        if seconds > 0:
            parts.append(f"{seconds} second{'s' if seconds != 1 else ''}")
        return ' '.join(parts)

if __name__ == '__main__':
    calculator = TimeDifferenceCalculator()
    duration_seconds = calculator.calculate_duration('2023-10-01 12:00:00', '2023-10-01 14:30:00')
    human_readable = calculator.format_duration(duration_seconds)
    print(f"Duration in seconds: {duration_seconds}")
    print(f"Human-readable duration: {human_readable}")