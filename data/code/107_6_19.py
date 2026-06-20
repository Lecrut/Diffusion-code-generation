from datetime import datetime

class DateFormatter:
    DATE_FORMAT = '%A, %B %d, %Y'
    
    def __init__(self, date_str):
        self.date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    
    def get_formatted_date(self):
        return self.date_obj.strftime(self.DATE_FORMAT)

if __name__ == '__main__':
    sample_date = '2023-10-05'
    formatter_instance = DateFormatter(sample_date)
    print(formatter_instance.get_formatted_date())