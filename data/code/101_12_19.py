def compute_day_index(year, month, day):
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    if day < 1 or day > 31:
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
    result = compute_day_index(1900, 1, 1)
    print(result)