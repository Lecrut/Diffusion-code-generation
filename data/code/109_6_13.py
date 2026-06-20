import datetime

class MonthFractionCalculator:
    @staticmethod
    def days_in_month(year, month):
        if month == 12:
            return 31
        else:
            next_month = (month % 12) + 1
            next_year = year + (month // 12)
            return (datetime.date(next_year, next_month, 1) - datetime.date(year, month, 1)).days

    @staticmethod
    def calculate_remaining_fraction(current_date, target_month):
        current_year = current_date.year
        current_month = current_date.month
        if target_month > current_month:
            target_year = current_year
            target_month_num = target_month
        elif target_month < current_month:
            target_year = current_year - 1
            target_month_num = target_month + 12
        else:
            target_year = current_year
            target_month_num = target_month

        if target_month_num == current_month:
            return 0.0

        days_in_current_month = MonthFractionCalculator.days_in_month(current_year, current_month)
        remaining_days = (datetime.date(target_year, target_month_num, 1) - current_date).days
        return remaining_days / days_in_current_month if days_in_current_month > 0 else 0.0

if __name__ == '__main__':
    calculator = MonthFractionCalculator()
    sample_date = datetime.date(2023, 4, 15)
    target_month = 6
    fraction_remaining = calculator.calculate_remaining_fraction(sample_date, target_month)
    print(fraction_remaining)