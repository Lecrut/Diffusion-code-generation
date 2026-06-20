from datetime import datetime

class DateFormatter:
    def format_date(self, date_str):
        return datetime.strptime(date_str, '%Y/%m/%d').strftime('%B %d, %Y')

if __name__ == '__main__':
    formatter = DateFormatter()
    sample_date1 = '2023/10/05'
    formatted_date1 = formatter.format_date(sample_date1)
    print(formatted_date1)
    sample_date2 = '1984/06/23'
    formatted_date2 = formatter.format_date(sample_date2)
    print(formatted_date2)