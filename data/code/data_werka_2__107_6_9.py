from datetime import datetime

class DateFormatter:
    def __init__(self, year, month, day):
        self.date_obj = datetime(year, month, day)
    
    def get_formatted_string(self):
        day_name = self.date_obj.strftime('%A')
        month_name = self.date_obj.strftime('%B')
        day_num = self.date_obj.day
        year_num = self.date_obj.year
        return f"{day_name}, {month_name} {day_num:02d}, {year_num}"
    
    def get_year(self):
        return self.date_obj.year
    
    def get_month_name(self):
        return self.date_obj.strftime('%B')

if __name__ == '__main__':
    formatter = DateFormatter(2023, 10, 25)
    print(formatter.get_formatted_string())
    print(formatter.get_year())
    print(formatter.get_month_name())