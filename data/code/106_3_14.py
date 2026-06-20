class DateDifferenceCalculator:
    DATE_FORMAT = "%Y-%m-%d"

    @staticmethod
    def calculate_age_difference(date_str1, date_str2):
        date1 = datetime.datetime.strptime(date_str1, DateDifferenceCalculator.DATE_FORMAT)
        date2 = datetime.datetime.strptime(date_str2, DateDifferenceCalculator.DATE_FORMAT)
        age_diff = abs((date2 - date1).days) // 365
        return age_diff

if __name__ == '__main__':
    calculator = DateDifferenceCalculator()
    print(calculator.calculate_age_difference("1990-05-15", "2023-04-10"))