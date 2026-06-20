from datetime import date

def days_difference(start_date_str: str, end_date_str: str) -> int:
    try:
        start_date = date.fromisoformat(start_date_str)
        end_date = date.fromisoformat(end_date_str)
        return (end_date - start_date).days
    except ValueError:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")

if __name__ == '__main__':
    try:
        days = days_difference('2023-01-01', '2023-01-31')
        print(days)
    except ValueError as e:
        print(e)