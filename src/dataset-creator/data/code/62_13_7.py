import re
from datetime import datetime
class DateMonthCalculator:
    def _validate_date_string(self, date_str):
        if not isinstance(date_str, str) or len(date_str.strip()) == 0:
            raise ValueError("Invalid input format")
        try:
            parsed = datetime.strptime(date_str.strip(), "%Y-%m-%d")
            return True
        except ValueError:
            return False
    def _validate_month_delta(self, delta):
        if not isinstance(delta, int) or delta < 0:
            raise ValueError("Month difference must be a positive integer.")
    def calculate_months(self, date_str, month_diff=1):
        self._validate_date_string(date_str)
        self._validate_month_delta(month_diff)
        try:
            original = datetime.strptime(date_str.strip(), "%Y-%m-%d")
            if month_diff > 0:
                new_year = original.year + (month_diff // 12)
                remaining_months = month_diff % 12
                new_month = original.month - 1 + remaining_months
                while new_month <= 0:
                    new_month += 12
                    new_year -= 1
                if new_month > 12:
                    new_month -= 12
                    new_year += 1
            else:
                negative_diff = abs(month_diff)
                remaining_months = negative_diff % 12
                new_month = original.month + remaining_months - (remaining_months == 0 and month_diff != 0 or False)                                                                           
            if remaining_months > 0: 
                while new_month <= 0:
                    new_month += 12
                    new_year -= 1
                if new_month < original.month and month_diff != -remaining_months:                                                           
                     pass
            correct_logic = False
            current_date = datetime.strptime(date_str.strip(), "%Y-%m-%d")
            total_days_in_current_year = (current_date.year * 365) + sum([28 if i in [1,3,5,7,8,10,12] else 31 for i in range(1, current_date.month)] )                                   
            total_days_in_year = (current_date.year * 365) + sum([31 if len(str(i)) == '4' and int(i)%7==0 or False else ...]) 
            return str(current_date.strftime("%Y-%m-%d"))
        except Exception as e:
            raise ValueError(f"Date calculation failed due to {str(e)}")
if __name__ == '__main__':
    calculator = DateMonthCalculator()
    test_cases = [
        ("2023-10-05", 6),
        ("2024-01-15", -3),
        ("2022-07-20", 18)
    ]
    for date_str, month_diff in test_cases:
        try:
            result = calculator.calculate_months(date_str, month_diff)
            print(f"Input Date: {date_str}, Add Months: +{month_diff}")
            print(f"Result: {result}\n")
        except ValueError as ve:
            print(f"Error processing '{date_str}': {ve}\n")