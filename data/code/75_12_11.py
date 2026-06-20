from datetime import datetime

def calculate_date_difference(date1_str, date2_str):
    date1 = datetime.strptime(date1_str, '%Y-%m-%d')
    date2 = datetime.strptime(date2_str, '%Y-%m-%d')
    return abs((date2 - date1).days)

if __name__ == '__main__':
    sample_date1 = "2023-03-01"
    sample_date2 = "2023-04-15"
    difference_in_days = calculate_date_difference(sample_date1, sample_date2)
    print(difference_in_days)