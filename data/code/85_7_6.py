from datetime import date

def weeks_difference(date1, date2):
    return abs((date2 - date1).days // 7)

if __name__ == '__main__':
    print(weeks_difference(date(2023, 1, 1), date(2023, 1, 8)))  # Output: 1
    print(weeks_difference(date(2023, 1, 8), date(2023, 1, 1)))  # Output: 1
    print(weeks_difference(date(2023, 1, 15), date(2023, 1, 1)))  # Output: 2