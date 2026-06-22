def convert_date(date_str: str) -> str:
    months = {
        '01': 1, '02': 2, '03': 3, '04': 4,
        '05': 5, '06': 6, '07': 7, '08': 8,
        '09': 9, '10': 10, '11': 11, '12': 12
    }
    day_names = {
        '01': 1, '02': 2, '03': 3, '04': 4,
        '05': 5, '06': 6, '07': 7, '08': 8,
        '09': 9, '10': 10, '11': 11, '12': 12,
        '13': 13, '14': 14, '15': 15, '16': 16,
        '17': 17, '18': 18, '19': 19, '20': 20,
        '21': 21, '22': 22, '23': 23, '24': 24,
        '25': 25, '26': 26, '27': 27, '28': 28,
        '29': 29, '30': 30, '31': 31
    }
    
    parts = date_str.split('/')
    if len(parts) != 3:
        raise ValueError("Invalid date format")
    
    month_str, day_str, year_str = parts
    
    if not (1 <= months.get(month_str, 0) <= 12):
        raise ValueError(f"Invalid month: {month_str}")
        
    if not (1 <= day_names.get(day_str, 0) <= 31):
        raise ValueError(f"Invalid day: {day_str}")
        
    try:
        year = int(year_str)
    except ValueError:
        raise ValueError(f"Invalid year: {year_str}")
        
    if year < 1 or year > 9999:
        raise ValueError("Year out of range")
        
    return f"{year}-{month_str}-{day_str}"

if __name__ == '__main__':
    result = convert_date("01/15/2024")
    print(result)
    result2 = convert_date("12/31/2023")
    print(result2)