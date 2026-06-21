class DateProcessor:
    def __init__(self, dates):
        self.dates = dates

    def get_days(self):
        days = []
        for date_str in self.dates:
            parts = date_str.split("-")
            year = int(parts[0])
            month = int(parts[1])
            day = int(parts[2])
            days.append(day)
        return days

if __name__ == '__main__':
    sample_dates = ["2021-05-12", "2022-08-30", "2023-01-01"]
    processor = DateProcessor(sample_dates)
    result = processor.get_days()
    print(result)