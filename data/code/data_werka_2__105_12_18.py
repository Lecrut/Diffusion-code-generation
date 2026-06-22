from datetime import datetime, timedelta
def next_weekday(date_str, target_weekday):
    ref = datetime.strptime(date_str, '%Y-%m-%d')
    delta = (target_weekday - ref.weekday()) % 7
    if delta == 0:
        delta = 7
    result = ref + timedelta(days=delta)
    return result.strftime('%Y-%m-%d')
if __name__ == '__main__':
    print(next_weekday('2023-10-01', 4))