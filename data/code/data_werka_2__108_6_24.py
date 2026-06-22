class DateProcessor:
    def __init__(self, dates):
        self.dates = dates

    def get_days(self):
        results = []
        for date_str in self.dates:
            parts = date_str.split("-")
            if len(parts) != 3:
                raise ValueError(f"Invalid format: {date_str}")
            try:
                year = int(parts[0])
                month = int(parts[1])
                day = int(parts[2])
            except ValueError:
                raise ValueError(f"Invalid numeric part in: {date_str}")
            
            if not (1 <= month <= 12):
                raise ValueError(f"Invalid month in: {date_str}")
            if not (1 <= day <= 31):
                raise ValueError(f"Invalid day in: {date_str}")
            
            if month in (4, 6, 9, 11) and day > 30:
                raise ValueError(f"Invalid day {day} for month {month} in: {date_str}")
            
            if month == 2:
                is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
                max_day = 29 if is_leap else 28
                if day > max_day:
                    raise ValueError(f"Invalid day {day} for month {month} in: {date_str}")
            
            results.append(day)
        return results

if __name__ == '__main__':
    sample_dates = ["2023-10-05", "2024-02-29", "2025-12-31"]
    processor = DateProcessor(sample_dates)
    print(processor.get_days())