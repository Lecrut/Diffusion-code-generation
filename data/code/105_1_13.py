import datetime

def find_first_sunday_after_jan_1_2024():
    base_date = datetime.date(2024, 1, 1)
    if base_date.weekday() == 6:
        return base_date + datetime.timedelta(days=7)
    days_to_add = 6 - base_date.weekday()
    return base_date + datetime.timedelta(days=days_to_add)

if __name__ == '__main__':
    result = find_first_sunday_after_jan_1_2024()
    print(result)