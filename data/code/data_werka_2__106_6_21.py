from datetime import datetime

def compute_year_difference(date_str1: str, date_str2: str) -> int:
    try:
        date1 = datetime.strptime(date_str1, "%Y-%m-%d")
        date2 = datetime.strptime(date_str2, "%Y-%m-%d")
    except ValueError as e:
        raise ValueError(f"Invalid date format. Expected YYYY-MM-DD. Error: {e}")
    
    diff = date2.year - date1.year
    
    if (date2.month, date2.day) < (date1.month, date1.day):
        diff -= 1
        
    return diff

if __name__ == '__main__':
    result = compute_year_difference("2020-02-29", "2023-02-28")
    print(result)