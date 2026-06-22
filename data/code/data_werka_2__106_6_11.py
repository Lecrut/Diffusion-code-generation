from datetime import datetime

def compute_year_difference(date1_str: str, date2_str: str) -> int:
    try:
        date1 = datetime.strptime(date1_str, "%Y-%m-%d")
        date2 = datetime.strptime(date2_str, "%Y-%m-%d")
    except ValueError as e:
        raise ValueError(f"Invalid date format. Expected YYYY-MM-DD. Error: {e}")
    
    diff = date2.year - date1.year
    
    if (date2.month, date2.day) < (date1.month, date1.day):
        diff -= 1
        
    return diff

if __name__ == '__main__':
    start_date = "2020-05-15"
    end_date = "2023-02-10"
    result = compute_year_difference(start_date, end_date)
    print(result)