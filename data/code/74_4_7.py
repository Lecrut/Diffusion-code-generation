from datetime import datetime

class DateProcessor:
    DAY_NAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    @staticmethod
    def get_full_day_name(date_obj):
        return DateProcessor.DAY_NAMES[date_obj.weekday()]

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 5)
    processor = DateProcessor()
    print(processor.get_full_day_name(sample_date))