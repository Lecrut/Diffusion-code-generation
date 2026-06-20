from datetime import date

def days_between(start_date, end_date):
    return (date.fromisoformat(end_date) - date.fromisoformat(start_date)).days

if __name__ == '__main__':
    print(days_between('2023-01-01', '2023-01-31'))