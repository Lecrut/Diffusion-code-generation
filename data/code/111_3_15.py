from datetime import date, timedelta

def subtract_three_months(start_date):
    return start_date - timedelta(days=3*30)

if __name__ == '__main__':
    sample_date = date(2023, 10, 15)
    result_date = subtract_three_months(sample_date)
    print(result_date)