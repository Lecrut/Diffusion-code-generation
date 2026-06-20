from datetime import datetime

class DateCalculator:
    MONTHS_PER_YEAR = 12
    
    @staticmethod
    def months_between_dates(date_str1, date_str2):
        date_format = "%Y-%m-%d"
        date1 = datetime.strptime(date_str1, date_format)
        date2 = datetime.strptime(date_str2, date_format)
        
        years_diff = date2.year - date1.year
        months_diff = date2.month - date1.month
        
        if date2.day < date1.day:
            months_diff -= 1
        
        total_months = (years_diff * DateCalculator.MONTHS_PER_YEAR) + months_diff
        return abs(total_months)

if __name__ == '__main__':
    print(DateCalculator.months_between_dates("2022-01-01", "2023-02-15"))