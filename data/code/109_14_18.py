import datetime

DAYS_IN_MONTH = {
    1: 31, 2: 28, 3: 31, 4: 30,
    5: 31, 6: 30, 7: 31, 8: 31,
    9: 30, 10: 31, 11: 30, 12: 31
}

def days_until_end_of_month(year, month):
    if month == 2 and (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        days_in_month[2] = 29
    return DAYS_IN_MONTH[month] - datetime.date(year, month, 1).day

if __name__ == '__main__':
    sample_year = 2023
    sample_month = 10
    print(f"Days left until the end of {sample_month}/{sample_year}: {days_until_end_of_month(sample_year, sample_month)} days")