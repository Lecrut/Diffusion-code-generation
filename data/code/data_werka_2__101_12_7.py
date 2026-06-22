DAY_NAMES = {0: "Saturday", 1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday"}

def get_day_of_week(year, month, day):
    if month < 3:
        month += 12
        year -= 1
    q = day
    m = month
    k = year % 100
    j = year // 100
    h = (q + (13 * (m + 1)) // 5 + k + (k // 4) + (j // 4) - (2 * j)) % 7
    return DAY_NAMES.get(h, "Unknown")

if __name__ == '__main__':
    result = get_day_of_week(1900, 1, 1)
    print(result)