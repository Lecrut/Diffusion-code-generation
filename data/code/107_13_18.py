from datetime import datetime

class DateFormatter:
    def format(self, date_str):
        date_obj = datetime.strptime(date_str, '%Y/%m/%d')
        return date_obj.strftime('%B %d, %Y')

if __name__ == '__main__':
    formatter = DateFormatter()
    sample_date = '2023/10/05'
    formatted_date = formatter.format(sample_date)
    print(formatted_date)