from datetime import datetime

class DateFormatFormatter:
    DATE_FORMAT = '%A, %B %d, %Y'
    
    @staticmethod
    def format_date(date_str):
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        return date_obj.strftime(DateFormatFormatter.DATE_FORMAT)

if __name__ == '__main__':
    sample_date = '2023-11-15'
    print(DateFormatFormatter.format_date(sample_date))