import datetime

class DateDifferenceCalculator:
    DATE_FORMAT = "%Y-%m-%d"

    @staticmethod
    def calculate_difference(date_str1, date_str2):
        date1 = datetime.datetime.strptime(date_str1, DateDifferenceCalculator.DATE_FORMAT).date()
        date2 = datetime.datetime.strptime(date_str2, DateDifferenceCalculator.DATE_FORMAT).date()
        
        if date1 > date2:
            start_date = date2
            end_date = date1
        else:
            start_date = date1
            end_date = date2
        
        time_difference = end_date - start_date
        return time_difference.days

if __name__ == '__main__':
    calculator = DateDifferenceCalculator()
    difference = calculator.calculate_difference("2023-01-15", "2021-11-20")
    print(f"Difference in days: {difference}")