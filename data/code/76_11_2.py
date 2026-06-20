from datetime import date

def days_difference(date1, date2):
    return (date.fromisoformat(date2) - date.fromisoformat(date1)).days

if __name__ == '__main__':
    print(days_difference('2023-01-01', '2023-01-31'))