from datetime import datetime

class DateCalculator:
    def validate_date_format(self, date_str):
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def calculate_difference(self, date1_str, date2_str):
        if not self.validate_date_format(date1_str) or not self.validate_date_format(date2_str):
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
        
        date1 = datetime.strptime(date1_str, "%Y-%m-%d")
        date2 = datetime.strptime(date2_str, "%Y-%m-%d")
        difference = abs((date2 - date1).days)
        return difference

if __name__ == '__main__':
    calculator = DateCalculator()
    date_a = "2023-01-01"
    date_b = "2023-01-10"
    difference = calculator.calculate_difference(date_a, date_b)
    print(difference)