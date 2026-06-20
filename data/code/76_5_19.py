import datetime

class DateDifferenceCalculator:
    DATE_FORMAT = '%m/%d/%Y'

    @staticmethod
    def calculate_date_difference(date_str1, date_str2):
        try:
            date1 = datetime.datetime.strptime(date_str1, DateDifferenceCalculator.DATE_FORMAT)
            date2 = datetime.datetime.strptime(date_str2, DateDifferenceCalculator.DATE_FORMAT)
            difference = abs((date1 - date2).days)
            return difference
        except ValueError:
            raise ValueError("Invalid date format. Please use MM/DD/YYYY.")

if __name__ == '__main__':
    calculator = DateDifferenceCalculator()
    print(f"Difference between 01/15/2023 and 03/20/2023: {calculator.calculate_date_difference('01/15/2023', '03/20/2023')} days")
    print(f"Difference between 12/31/2022 and 01/01/2023: {calculator.calculate_date_difference('12/31/2022', '01/01/2023')} days")