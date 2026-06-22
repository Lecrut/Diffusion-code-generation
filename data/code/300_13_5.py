def days_remaining_in_february(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return 29
    else:
        return 28
if __name__ == '__main__':
    print(days_remaining_in_february(2023))
    print(days_remaining_in_february(2024))