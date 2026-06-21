def get_day_of_month(date_obj):
    return date_obj.day

def extract_day_components(year, month, day):
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        raise ValueError("Inputs must be integers")
    if month < 1 or month > 12:
        raise ValueError("Invalid month")
    if day < 1:
        raise ValueError("Invalid day")
    days_in_months = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    max_day = days_in_months[month - 1]
    if month == 2 and is_leap:
        max_day += 1
    if day > max_day:
        raise ValueError("Day out of range")
    return day

class DateExtractor:
    def __init__(self, date_obj):
        self.date_obj = date_obj

    def get_day(self):
        return self.date_obj.day

if __name__ == '__main__':
    import datetime
    sample_date = datetime.date(1999, 12, 31)
    result_func = get_day_of_month(sample_date)
    print(result_func)
    extractor = DateExtractor(sample_date)
    result_class = extractor.get_day()
    print(result_class)