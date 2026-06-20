def calculate_day_of_year(year, month, day):
    months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        months[2] += 1
    return sum(months[:month]) + day

if __name__ == '__main__':
    sample_year = 2023
    sample_month = 7
    sample_day = 4
    result = calculate_day_of_year(sample_year, sample_month, sample_day)
    print(result)