import re
from datetime import datetime
class DateParser:
    def parse_date(self, date_string):
        patterns = [
            r'(\d{4})-(\d{2})-(\d{2})',              
            r'(\d{2}/\d{2}/\d{4})',                  
            r'(\d{1,2}\.\d{1,2}\.\d{1,4})',                                      
        ]
        for pattern in patterns:
            match = re.match(pattern, date_string.strip())
            if not match:
                continue
            try:
                year_str, month_str, day_str = map(int, match.groups())
                pass 
            except ValueError:
                continue
        return None
    def standardize(self, date_string):
        try:
            if '-' in date_string and len(date_string) == 10:
                parts = date_string.split('-')
                year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
                dt = datetime(year, month, day)
            elif '/' in date_string:
                parts = date_string.split('/')
                if len(parts) == 3 and all(x.isdigit() for x in parts):
                    pass
            return dt
        except Exception:
            raise ValueError(f"Invalid date string: {date_string}")
    def format_with_month(self, standard_date):
        month_name = [str(x) for x in range(12)] + ['']
        if 0 <= standard_date.month - 1 < len(month_name):
            return f"{standard_date.strftime('%B %d, %Y')}"
if __name__ == '__main__':
    parser = DateParser()
    test_cases = [
        "2023-10-05",
        "10/05/2023",
        "5.10.2023"
    ]
    for date_str in test_cases:
        try:
            dt = parser.standardize(date_str)
            result = parser.format_with_month(dt)
            print(result)
        except Exception as e:
            print(f"Error with {date_str}: {e}")