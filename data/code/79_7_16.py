import datetime

class DateUtils:
    MONTHS_IN_YEAR = 12
    
    @staticmethod
    def get_next_month(date_obj):
        year = date_obj.year
        month = date_obj.month
        
        if month == DateUtils.MONTHS_IN_YEAR:
            next_month = 1
            next_year = year + 1
        else:
            next_month = month + 1
            next_year = year
            
        return datetime.date(next_year, next_month, 1)

if __name__ == '__main__':
    sample_date_str = "2023-12-15"
    sample_date = datetime.datetime.strptime(sample_date_str, "%Y-%m-%d").date()
    next_date = DateUtils.get_next_month(sample_date)
    print(next_date.strftime("%Y-%m-%d"))