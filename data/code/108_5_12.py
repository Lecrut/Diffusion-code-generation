from datetime import datetime

class DateProcessor:
    def __init__(self, date: datetime):
        self.date = date
    
    def get_day_of_month(self) -> int:
        return self.date.day

if __name__ == '__main__':
    sample_date = datetime(2023, 9, 15)
    processor = DateProcessor(sample_date)
    print(processor.get_day_of_month())