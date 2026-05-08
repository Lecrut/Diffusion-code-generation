from datetime import date, timedelta
class DateCalculator:
    def calculate_time_remaining_in_month(self, current_date: date) -> int:
        today = current_date
        if today.month == 12:
            next_month = today.replace(year=today.year + 1, month=1, day=1)
        else:
            next_month = today.replace(month=today.month + 1, day=1)
        time_remaining = (next_month - today).days
        return time_remaining
if __name__ == '__main__':
    calculator = DateCalculator()
    sample_date_1 = date(2023, 10, 15)
    remaining_1 = calculator.calculate_time_remaining_in_month(sample_date_1)
    print(f"Time remaining from {sample_date_1} until the end of the month: {remaining_1} days")
    sample_date_2 = date(2024, 1, 5)
    remaining_2 = calculator.calculate_time_remaining_in_month(sample_date_2)
    print(f"Time remaining from {sample_date_2} until the end of the month: {remaining_2} days")
    sample_date_3 = date(2023, 12, 20)
    remaining_3 = calculator.calculate_time_remaining_in_month(sample_date_3)
    print(f"Time remaining from {sample_date_3} until the end of the month: {remaining_3} days")