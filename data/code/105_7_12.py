from datetime import date, timedelta

def find_next_tuesday(anchor: date) -> date:
    current = anchor.weekday()
    offset = (1 - current) % 7
    if offset == 0:
        offset = 7
    return anchor + timedelta(days=offset)

if __name__ == '__main__':
    start = date(2023, 7, 4)
    next_tue = find_next_tuesday(start)
    print(next_tue)