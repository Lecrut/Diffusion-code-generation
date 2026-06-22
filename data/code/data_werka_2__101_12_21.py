def calculate_zeller_day(year, month, day):
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    if not (1 <= day <= 31):
        raise ValueError("Day must be between 1 and 31")
    if year < 1:
        raise ValueError("Year must be positive")
    if month < 3:
        month += 12
        year -= 1
    k = year % 100
    j = year // 100
    h = (day + (13 * (month + 1)) // 5 + k + k // 4 + j // 4 - 2 * j) % 7
    return h

if __name__ == '__main__':
    result = calculate_zeller_day(1900, 1, 1)
    print(result)