from datetime import datetime, timedelta

def find_next_weekday(current_date_str: str, target_weekday: int) -> str:
    current_dt = datetime.strptime(current_date_str, '%Y-%m-%d')
    current_weekday_index = current_dt.weekday()
    days_to_add = (target_weekday - current_weekday_index) % 7
    if days_to_add == 0:
        days_to_add = 7
    target_dt = current_dt + timedelta(days=days_to_add)
    return target_dt.strftime('%Y-%m-%d')

if __name__ == '__main__':
    reference = '2024-02-10'
    target = 5
    output = find_next_weekday(reference, target)
    print(output)