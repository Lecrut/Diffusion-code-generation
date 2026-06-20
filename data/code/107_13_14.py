from datetime import datetime

class DateFormatter:
    def __init__(self, date_str):
        self.date_obj = datetime.strptime(date_str, '%Y/%m/%d')

    def format(self):
        return self.date_obj.strftime('%B %d, %Y')

if __name__ == '__main__':
    sample_date = '2023/10/05'
    formatter = DateFormatter(sample_date)
    formatted_date = formatter.format()
    print(formatted_date)