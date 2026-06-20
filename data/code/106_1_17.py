from datetime import date

class YearDifferenceCalculator:
    def calculate_year_difference(self, date_str1, date_str2):
        date_format = "%Y-%m-%d"
        date1 = date.strptime(date_str1, date_format)
        date2 = date.strptime(date_str2, date_format)
        return abs((date2 - date1).days // 365)

if __name__ == '__main__':
    calculator = YearDifferenceCalculator()
    print(calculator.calculate_year_difference("2023-04-15", "1990-07-23"))
    print(calculator.calculate_year_difference("2000-12-31", "2024-01-01"))
    print(calculator.calculate_year_difference("1850-01-01", "1900-01-01"))