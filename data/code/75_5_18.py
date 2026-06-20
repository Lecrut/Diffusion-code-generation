import datetime

def calculate_date_difference(date1, date2):
    return (date2 - date1).days
if __name__ == '__main__':
    sample_date1 = datetime.date(2023, 10, 1)
    sample_date2 = datetime.date(2023, 10, 15)
    result = calculate_date_difference(sample_date1, sample_date2)
    print(result)