from datetime import date, timedelta

def add_days_to_base_date(reference: date, offset: int) -> str:
    final_date = reference + timedelta(days=offset)
    return final_date.strftime("%Y-%m-%d")

if __name__ == '__main__':
    base = date(2024, 7, 4)
    days_offset = 30
    output = add_days_to_base_date(base, days_offset)
    print(output)