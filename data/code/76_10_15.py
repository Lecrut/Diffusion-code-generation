from datetime import datetime

class DateCalculator:

    def get_difference(self, date1_str, date2_str):
        try:
            date1 = datetime.strptime(date1_str, '%Y-%m-%d')
            date2 = datetime.strptime(date2_str, '%Y-%m-%d')
            diff = abs((date2 - date1).days)
            return diff
        except ValueError:
            raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")
if __name__ == '__main__':
    calculator = DateCalculator()
    date1_str = '2023-01-01'
    date2_str = '2023-01-10'
    result = calculator.get_difference(date1_str, date2_str)
    print(result)
    try:
        date3_str = '2024-12-31'
        date4_str = '2024-01-01'
        result = calculator.get_difference(date3_str, date4_str)
        print(result)
    except ValueError as e:
        print(e)