from datetime import datetime

class DayOfWeek:
    DAY_NAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    def get_full_day_name(self, date_obj):
        return self.DAY_NAMES[date_obj.weekday()]

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 5)
    day_info = DayOfWeek()
    print(day_info.get_full_day_name(sample_date))