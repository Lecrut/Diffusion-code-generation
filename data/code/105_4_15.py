from datetime import date, timedelta

def compute_next_saturday(start: date) -> date:
    current_weekday = start.weekday()
    target_weekday = 5
    days_offset = (target_weekday - current_weekday) % 7
    return start + timedelta(days=days_offset)

if __name__ == '__main__':
    reference = date(2023, 11, 1)
    answer = compute_next_saturday(reference)
    print(answer)