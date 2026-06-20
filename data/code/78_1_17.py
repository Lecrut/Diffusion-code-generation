from datetime import date

class MonthCalculator:
    MONTH_MAP = {
        'January': 1, 'February': 2, 'March': 3, 'April': 4,
        'May': 5, 'June': 6, 'July': 7, 'August': 8,
        'September': 9, 'October': 10, 'November': 11, 'December': 12
    }
    
    @staticmethod
    def calculate_month_difference(month1_str, month2_str):
        try:
            month1 = MonthCalculator.MONTH_MAP[month1_str]
            month2 = MonthCalculator.MONTH_MAP[month2_str]
            return abs(month1 - month2)
        except KeyError:
            raise ValueError("Invalid month string provided. Please use full month names.")

if __name__ == '__main__':
    calculator = MonthCalculator()
    month_a = 'January'
    month_b = 'March'
    difference = calculator.calculate_month_difference(month_a, month_b)
    print(f"Difference between {month_a} and {month_b}: {difference}")