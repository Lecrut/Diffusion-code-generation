import datetime
def manipulate_date(start_date, days_to_change):
    new_date = start_date + datetime.timedelta(days=days_to_change)
    return new_date
start_date = datetime.date(2023, 10, 27)
print(f"Original Date: {start_date}")
future_date = manipulate_date(start_date, 30)
print(f"Date after adding 30 days: {future_date}")
past_date = manipulate_date(start_date, -15)
print(f"Date after subtracting 15 days: {past_date}")
print("-" * 20)
start_date_month = datetime.date(2024, 1, 15)
print(f"Original Date (Month focus): {start_date_month}")
future_month = manipulate_date(start_date_month, 60)
print(f"Date after adding 60 days: {future_month}")
past_month = manipulate_date(start_date_month, -30)
print(f"Date after subtracting 30 days: {past_month}")
if __name__ == '__main__':
    pass