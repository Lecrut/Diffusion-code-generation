from datetime import date, timedelta

def calculate_next_friday(reference_date):
    reference_datetime = date.strptime(reference_date, "%B %d, %Y")
    days_until_friday = (4 - reference_datetime.weekday()) % 7
    if days_until_friday == 0:
        days_until_friday = 7
    return (reference_datetime + timedelta(days=days_until_friday)).strftime("%B %d, %Y")

if __name__ == '__main__':
    sample_date = "December 15, 2023"
    next_friday = calculate_next_friday(sample_date)
    print(next_friday)