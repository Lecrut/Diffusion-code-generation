from datetime import datetime

def calculate_year_difference(date_str1, date_str2):
    date_format = "%Y-%m-%d"
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    return abs((date2 - date1).days // 365)

if __name__ == '__main__':
    sample_dates = {
        "sample1": ("2023-04-15", "1998-11-20"),
        "sample2": ("2000-07-01", "2024-03-15"),
        "sample3": ("1850-01-01", "1900-05-30")
    }
    
    for key, (date1, date2) in sample_dates.items():
        result = calculate_year_difference(date1, date2)
        print(f"{key}: {result}")