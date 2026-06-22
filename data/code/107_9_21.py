import calendar

MONTHS = {
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

def transform_date(date_input):
    components = date_input.split('-')
    year_val = int(components[0])
    month_val = int(components[1])
    day_val = int(components[2])
    
    if month_val not in MONTHS:
        raise ValueError(f"Invalid month: {month_val}")
        
    month_text = MONTHS[month_val]
    return f"{month_text} {day_val:02d}, {year_val}"

if __name__ == '__main__':
    print(transform_date('2023-1-5'))
    print(transform_date('2024-12-25'))
    print(transform_date('2000-2-29'))