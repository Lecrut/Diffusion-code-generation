from datetime import datetime

class DateCalculator:
    @staticmethod
    def get_difference(date1_str: str, date2_str: str) -> int:
        try:
            date1 = datetime.strptime(date1_str, '%Y-%m-%d')
            date2 = datetime.strptime(date2_str, '%Y-%m-%d')
            diff = abs((date1 - date2).days)
            return diff
        except ValueError:
            return -1

if __name__ == '__main__':
    calc = DateCalculator()
    print(calc.get_difference("2023-01-01", "2023-01-10"))
    print(calc.get_difference("2024-12-31", "2024-01-01"))