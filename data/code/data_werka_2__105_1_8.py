import datetime

def find_first_sunday_after_start():
    anchor = datetime.date(2024, 1, 1)
    day_index = anchor.weekday()
    days_to_add = 6 - day_index
    if days_to_add <= 0:
        days_to_add += 7
    target = anchor + datetime.timedelta(days=days_to_add)
    return target

if __name__ == '__main__':
    base_point = datetime.date(2024, 1, 1)
    result_date = find_first_sunday_after_start()
    print(result_date)