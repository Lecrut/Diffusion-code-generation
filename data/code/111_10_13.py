from datetime import datetime

def calculate_days_difference(date_str1, date_str2):
    date_format = '%Y-%m-%d'
    date1_obj = datetime.strptime(date_str1, date_format)
    date2_obj = datetime.strptime(date_str2, date_format)
    delta = abs((date2_obj - date1_obj).days)
    return delta

if __name__ == '__main__':
    sample_date1 = "2023-09-15"
    sample_date2 = "2023-10-20"
    days_diff = calculate_days_difference(sample_date1, sample_date2)
    print(f"Days between {sample_date1} and {sample_date2}: {days_diff}")