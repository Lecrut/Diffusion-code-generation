import calendar

MONTH_NAMES = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}

def reformat_date(date_str: str) -> str:
    parts = date_str.split('-')
    if len(parts) != 3:
        raise ValueError("Invalid date format")
    
    year = int(parts[0])
    month = int(parts[1])
    day = int(parts[2])
    
    if not (1 <= month <= 12):
        raise ValueError("Invalid month")
        
    month_name = MONTH_NAMES[month]
    
    return f"{month_name} {day:02d}, {year}"

if __name__ == '__main__':
    print(reformat_date('2023-1-5'))
    print(reformat_date('2024-12-25'))
    print(reformat_date('2000-2-29'))