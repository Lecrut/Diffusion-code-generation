from datetime import datetime
SECONDS_PER_YEAR = 31536000

def calculate_year_difference(date_str1, date_str2):
    date_format = '%Y-%m-%d'
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    return abs((date2 - date1).days) // SECONDS_PER_YEAR
if __name__ == '__main__':
    sample_date1 = '1990-05-15'
    sample_date2 = '2023-04-10'
    print(calculate_year_difference(sample_date1, sample_date2))