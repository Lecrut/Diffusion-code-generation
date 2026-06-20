import datetime

def calculate_days_difference(date1_str, date2_str):
    formats = ['%m/%d/%Y', '%Y-%m-%d']
    for fmt in formats:
        try:
            date1 = datetime.datetime.strptime(date1_str, fmt)
            date2 = datetime.datetime.strptime(date2_str, fmt)
            break
        except ValueError:
            continue
    else:
        raise ValueError('Invalid date format. Please use MM/DD/YYYY or YYYY-MM-DD.')
    
    return abs((date2 - date1).days)

if __name__ == '__main__':
    date1 = "2023-01-15"
    date2 = "2024-03-20"
    result = calculate_days_difference(date1, date2)
    print(result)