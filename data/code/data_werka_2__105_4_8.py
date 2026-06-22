from datetime import date, timedelta

def get_next_saturday(ref_date: date) -> date:
    current_weekday = ref_date.weekday()
    if current_weekday == 5:
        return ref_date
    days_to_add = (5 - current_weekday) % 7
    return ref_date + timedelta(days=days_to_add)

if __name__ == '__main__':
    target_date = date(2023, 11, 1)
    result = get_next_saturday(target_date)
    print(result)