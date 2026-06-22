def calculate_day_number(month):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days_in_month[month]

if __name__ == '__main__':
    sample_month = 5
    print(f"Day number in month {sample_month}: {calculate_day_number(sample_month)}")