from datetime import date, timedelta

class DateCalculator:
    def get_next_month_date(self, input_date):
        if input_date.month == 12:
            return date(input_date.year + 1, 1, 1)
        else:
            return date(input_date.year, input_date.month + 1, 1)

if __name__ == '__main__':
    calculator = DateCalculator()
    sample_date_1 = date(2023, 5, 15)
    print(f"Next month after {sample_date_1}: {calculator.get_next_month_date(sample_date_1)}")
    sample_date_2 = date(2024, 11, 30)
    print(f"Next month after {sample_date_2}: {calculator.get_next_month_date(sample_date_2)}")