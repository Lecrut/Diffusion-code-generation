from datetime import datetime

def calculate_age_difference(date_str1, date_str2):
    date_format = "%Y-%m-%d"
    birth_date = datetime.strptime(date_str1, date_format)
    current_date = datetime.strptime(date_str2, date_format)
    age_diff = abs((current_date - birth_date).days) // 365
    return age_diff

if __name__ == '__main__':
    sample_date1 = "1980-07-22"
    sample_date2 = "2023-10-05"
    print(calculate_age_difference(sample_date1, sample_date2))