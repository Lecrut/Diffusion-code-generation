from datetime import datetime

class DateCalculator:
    DATE_FORMAT = "%Y-%m-%d"
    
    def days_between(self, date1_str: str, date2_str: str) -> int:
        date1 = datetime.strptime(date1_str, self.DATE_FORMAT)
        date2 = datetime.strptime(date2_str, self.DATE_FORMAT)
        return abs((date2 - date1).days)

if __name__ == '__main__':
    calculator = DateCalculator()
    print(calculator.days_between("2023-01-01", "2023-01-15"))