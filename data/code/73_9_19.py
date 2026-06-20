from datetime import datetime

class DateDifferenceCalculator:
    @staticmethod
    def calculate_time_difference(date_str1, date_str2):
        try:
            date1 = datetime.strptime(date_str1, '%Y-%m-%d')
            date2 = datetime.strptime(date_str2, '%Y-%m-%d')
            difference = abs(date1 - date2)
            return difference
        except ValueError:
            raise ValueError("Error: Invalid date format. Please use YYYY-MM-DD.")

if __name__ == '__main__':
    calculator = DateDifferenceCalculator()
    date_a = "2023-01-15"
    date_b = "2023-02-20"
    print(f"Difference between {date_a} and {date_b}: {calculator.calculate_time_difference(date_a, date_b)}")