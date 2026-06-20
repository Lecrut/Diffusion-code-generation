from datetime import datetime, timedelta

class DateHelper:
    MONTHS = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    @staticmethod
    def get_next_month(date_str):
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        year, month, day = date_obj.year, date_obj.month, date_obj.day
        
        if month == 12:
            next_year = year + 1
            next_month = 1
        else:
            next_year = year
            next_month = month + 1
        
        if day > DateHelper.MONTHS[next_month]:
            day = DateHelper.MONTHS[next_month]
        
        return datetime(next_year, next_month, day).strftime("%Y-%m-%d")

if __name__ == '__main__':
    helper = DateHelper()
    sample_date1 = "2023-10-15"
    sample_date2 = "2023-12-31"
    sample_date3 = "2024-01-01"
    next_month1 = helper.get_next_month(sample_date1)
    next_month2 = helper.get_next_month(sample_date2)
    next_month3 = helper.get_next_month(sample_date3)
    print(f"Next month after {sample_date1}: {next_month1}")
    print(f"Next month after {sample_date2}: {next_month2}")
    print(f"Next month after {sample_date3}: {next_month3}")