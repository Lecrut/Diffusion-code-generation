class DateParser:
    MONTH_DAYS = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    @staticmethod
    def _is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    @staticmethod
    def _parse_date(date_str):
        if len(date_str) != 10 or date_str[4] != '-' or date_str[7] != '-':
            raise ValueError("Invalid date format")
        year = int(date_str[0:4])
        month = int(date_str[5:7])
        day = int(date_str[8:10])
        
        if month < 1 or month > 12:
            raise ValueError("Invalid month")
        
        days_in_month = DateParser.MONTH_DAYS[month]
        if month == 2 and DateParser._is_leap_year(year):
            days_in_month += 1
            
        if day < 1 or day > days_in_month:
            raise ValueError("Invalid day")
            
        return year, month, day

def compute_year_difference(date1_str: str, date2_str: str) -> int:
    y1, _, _ = DateParser._parse_date(date1_str)
    y2, _, _ = DateParser._parse_date(date2_str)
    return abs(y1 - y2)

if __name__ == '__main__':
    result = compute_year_difference("2000-02-29", "2004-03-01")
    print(result)