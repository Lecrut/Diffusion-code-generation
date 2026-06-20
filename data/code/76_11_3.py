from datetime import date

def days_difference(start_date_str, end_date_str):
    start_date = date.fromisoformat(start_date_str)
    end_date = date.fromisoformat(end_date_str)
    return (end_date - start_date).days

if __name__ == '__main__':
    print(days_difference('2023-01-01', '2023-01-31'))