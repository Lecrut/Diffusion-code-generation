from datetime import datetime

def calculate_days_difference(date1_str, date2_str):
    date_format = '%Y-%m-%d'
    date1_obj = datetime.strptime(date1_str, date_format)
    date2_obj = datetime.strptime(date2_str, date_format)
    delta = abs((date2_obj - date1_obj).days)
    return delta

if __name__ == '__main__':
    date1_sample = "2023-09-01"
    date2_sample = "2023-10-15"
    days_diff = calculate_days_difference(date1_sample, date2_sample)
    print(f"Days between {date1_sample} and {date2_sample}: {days_diff}")