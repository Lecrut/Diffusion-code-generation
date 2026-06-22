def calculate_zeller(year, month, day):
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    if not (1 <= day <= 31):
        raise ValueError("Day must be between 1 and 31")
    if year < 1:
        raise ValueError("Year must be positive")
    
    adjusted_month = month
    adjusted_year = year
    
    if month < 3:
        adjusted_month += 12
        adjusted_year -= 1
        
    k = adjusted_year % 100
    j = adjusted_year // 100
    
    h = (day + (13 * (adjusted_month + 1)) // 5 + k + k // 4 + j // 4 - 2 * j) % 7
    return h

if __name__ == '__main__':
    result = calculate_zeller(1900, 1, 1)
    print(result)