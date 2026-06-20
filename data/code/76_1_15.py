import datetime

class DateCalculator:
    DATE_FORMAT = "%Y-%m-%d"
    
    def validate_date(self, date_str):
        try:
            datetime.datetime.strptime(date_str, self.DATE_FORMAT)
            return True
        except ValueError:
            return False
    
    def days_between(self, date1_str, date2_str):
        if not (self.validate_date(date1_str) and self.validate_date(date2_str)):
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
        
        date1 = datetime.datetime.strptime(date1_str, self.DATE_FORMAT)
        date2 = datetime.datetime.strptime(date2_str, self.DATE_FORMAT)
        return abs((date2 - date1).days)

if __name__ == '__main__':
    calculator = DateCalculator()
    print(calculator.days_between("2023-01-01", "2023-01-15"))