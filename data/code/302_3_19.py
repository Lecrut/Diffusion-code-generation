def days_in_month(year):
    month_days = {
        1: 31, 2: 28, 3: 31, 4: 30, 
        5: 31, 6: 30, 7: 31, 8: 31, 
        9: 30, 10: 31, 11: 30, 12: 31
    }
    month_days[2] += (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    return month_days

if __name__ == '__main__':
    sample_year = 2024
    print(days_in_month(sample_year))