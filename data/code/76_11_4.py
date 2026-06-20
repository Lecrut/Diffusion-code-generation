from datetime import date

def calculate_days(start_date_str, end_date_str):
    start_date = date.fromisoformat(start_date_str)
    end_date = date.fromisoformat(end_date_str)
    return (end_date - start_date).days

if __name__ == '__main__':
    start = "2023-01-01"
    end = "2023-01-15"
    days = calculate_days(start, end)
    print(days)