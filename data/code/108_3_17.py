import re

class DateParser:
    DATE_PATTERN = r'^\d{4}-\d{2}-\d{2}$'

    @staticmethod
    def extract_day(date_str):
        if not re.match(DateParser.DATE_PATTERN, date_str):
            raise ValueError("Invalid date format. Expected YYYY-MM-DD")
        
        return int(date_str.split('-')[2])

if __name__ == '__main__':
    sample_date1 = '2023-04-15'
    result1 = DateParser.extract_day(sample_date1)
    print(f"Date: {sample_date1}, Day of the month: {result1}")
    
    sample_date2 = '2023-12-31'
    result2 = DateParser.extract_day(sample_date2)
    print(f"Date: {sample_date2}, Day of the month: {result2}")