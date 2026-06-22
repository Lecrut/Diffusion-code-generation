import datetime

def compute_year_difference(date1_str: str, date2_str: str) -> int:
    try:
        date1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d").date()
        date2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d").date()
    except ValueError as e:
        raise ValueError(f"Invalid date format. Expected YYYY-MM-DD. Error: {e}")
    
    years_diff = date2.year - date1.year
    
    if (date2.month, date2.day) < (date1.month, date1.day):
        years_diff -= 1
        
    return abs(years_diff)

if __name__ == '__main__':
    d1 = "2020-02-29"
    d2 = "2023-03-01"
    result = compute_year_difference(d1, d2)
    print(result)