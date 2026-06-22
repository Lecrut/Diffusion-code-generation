from datetime import date

def days_remaining_in_month(current_date):
    next_month = current_date.replace(day=28) + timedelta(days=4)
    return (next_month - current_date).days

if __name__ == '__main__':
    sample_date = date(2023, 10, 15)
    print(days_remaining_in_month(sample_date))