from datetime import datetime

def compare_dates(date_str1, date_str2):
    try:
        date1 = datetime.strptime(date_str1, '%Y-%m-%d')
        date2 = datetime.strptime(date_str2, '%Y-%m-%d')
        return min(date1, date2)
    except ValueError:
        return None

if __name__ == '__main__':
    date_a = "2023-10-26"
    date_b = "2023-10-25"
    result1 = compare_dates(date_a, date_b)
    print(f"Comparing {date_a} and {date_b}: {result1}")
    
    date_c = "2024-01-01"
    date_d = "2023-12-31"
    result2 = compare_dates(date_c, date_d)
    print(f"Comparing {date_c} and {date_d}: {result2}")