from datetime import date, timedelta

def find_upcoming_saturday(input_date):
    current_weekday_index = input_date.weekday()
    saturday_weekday_index = 5
    difference = saturday_weekday_index - current_weekday_index
    if difference <= 0:
        difference += 7
    offset = timedelta(days=difference)
    return input_date + offset

if __name__ == '__main__':
    base_date = date(2023, 11, 1)
    result = find_upcoming_saturday(base_date)
    print(result)