from datetime import datetime

def days_difference(date1_str, date2_str):
    date_format = '%Y-%m-%d'
    date1_obj = datetime.strptime(date1_str, date_format)
    date2_obj = datetime.strptime(date2_str, date_format)
    delta = abs((date2_obj - date1_obj).days)
    return delta

if __name__ == '__main__':
    date_pairs = {
        ('2023-10-01', '2023-10-15'): None,
        ('2023-11-01', '2023-11-15'): None
    }
    
    for (date1, date2), _ in date_pairs.items():
        print(f"Days between {date1} and {date2}: {days_difference(date1, date2)}")