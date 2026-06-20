from datetime import datetime

class DateCalculator:

    @staticmethod
    def is_valid_date(date_str):
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def get_difference(self, date1_str, date2_str):
        if not (self.is_valid_date(date1_str) and self.is_valid_date(date2_str)):
            return -1
        date1 = datetime.strptime(date1_str, '%Y-%m-%d')
        date2 = datetime.strptime(date2_str, '%Y-%m-%d')
        diff = abs((date1 - date2).days)
        return diff
if __name__ == '__main__':
    calculator = DateCalculator()
    result = calculator.get_difference('2023-01-01', '2023-01-10')
    print(result)
    result = calculator.get_difference('2024-12-31', '2024-01-01')
    print(result)