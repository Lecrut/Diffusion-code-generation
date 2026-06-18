import datetime
def calculate_date_difference(days_a: int, days_b: int) -> float:
    date_a = datetime.date(1970, 1, 1) + datetime.timedelta(days=days_a)
    date_b = datetime.date(1970, 1, 1) + datetime.timedelta(days=days_b)
    return abs((date_b - date_a).days)
if __name__ == '__main__':
    sample_days_1 = 365 * 24                                      
    sample_days_2 = 365 * 25 + 10
    result = calculate_date_difference(sample_days_1, sample_days_2)
    print(result)