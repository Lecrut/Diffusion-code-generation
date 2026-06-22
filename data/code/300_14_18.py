def days_in_month(year: int, month: int) -> int:
    if month == 2:
        is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        return 29 if is_leap_year else 28
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    else:
        return 30

if __name__ == '__main__':
    sample_year_1 = 2023
    sample_month_1 = 10
    print(f"Year: {sample_year_1}, Month: {sample_month_1}, Days in month: {days_in_month(sample_year_1, sample_month_1)}")
    
    sample_year_2 = 2024
    sample_month_2 = 2
    print(f"Year: {sample_year_2}, Month: {sample_month_2}, Days in month: {days_in_month(sample_year_2, sample_month_2)}")