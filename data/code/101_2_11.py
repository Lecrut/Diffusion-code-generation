def calculate_day_of_week(year, month, day):
    if month < 3:
        year -= 1
        month += 12
    
    q = day
    m = month
    k = year % 100
    j = year // 100
    
    f = q + ((13 * (m + 1)) // 5) + k + (k // 4) + (j // 4) - (2 * j)
    
    day_of_week_index = f % 7
    return day_of_week_index

if __name__ == '__main__':
    year = 2024
    month = 2
    day = 29
    
    day_index = calculate_day_of_week(year, month, day)
    print(f"Date: {year}-{month:02d}-{day:02d}, Day Index (Monday=0): {day_index}")