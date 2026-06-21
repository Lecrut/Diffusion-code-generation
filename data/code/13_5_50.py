from datetime import date

def calculate_duration(start_date_str, end_date_str):
    start_date = date.fromisoformat(start_date_str)
    end_date = date.fromisoformat(end_date_str)
    delta = end_date - start_date
    return delta.days

if __name__ == '__main__':
    start_date = '2020-01-01'
    end_date = '2024-01-01'
    duration = calculate_duration(start_date, end_date)
    print(duration)