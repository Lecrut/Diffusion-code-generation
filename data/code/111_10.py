import datetime
def manipulate_date(start_date, days_to_change):
    new_date = start_date + datetime.timedelta(days=days_to_change)
    return new_date
start_date = datetime.date(2023, 10, 26)
print(f"Original Date: {start_date}")
print("\n--- Incrementing Date ---")
increment_days = 10
new_date_increment = manipulate_date(start_date, increment_days)
print(f"Date after adding {increment_days} days: {new_date_increment}")
print("\n--- Decrementing Date ---")
decrement_days = -5
new_date_decrement = manipulate_date(start_date, decrement_days)
print(f"Date after subtracting {abs(decrement_days)} days: {new_date_decrement}")
print("\n--- Manipulating Month and Year Directly (Demonstration) ---")
current_year = start_date.year
current_month = start_date.month
current_day = start_date.day
new_year = current_year + 1
new_month = current_month + 1
new_day = current_day
if new_month > 12:
    new_month = 1
    new_year += 1
print(f"Original components: Year={current_year}, Month={current_month}, Day={current_day}")
print(f"New components (incremented by one month): Year={new_year}, Month={new_month}, Day={new_day}")
if __name__ == '__main__':
    pass