from datetime import datetime

class DateFormatter:
    DATE_FORMAT = '%A, %B %d, %Y'
    
    def format_date(self, date_str):
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        return date_obj.strftime(self.DATE_FORMAT)

if __name__ == '__main__':
    formatter = DateFormatter()
    sample_date = '2023-10-05'
    print(formatter.format_date(sample_date))