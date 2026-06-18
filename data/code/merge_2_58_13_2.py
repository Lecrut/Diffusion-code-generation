from datetime import date
def calculate_days_difference(date1: date, date2: date) -> int:
    return abs((date2 - date1).days)
if __name__ == '__main__':
    sample_date_1 = date(2023, 5, 15)
    sample_date_2 = date(2024, 8, 20)
    result = calculate_days_difference(sample_date_1, sample_date_2)
    print(result)