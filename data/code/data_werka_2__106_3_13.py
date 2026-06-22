from datetime import date

def calculate_year_difference(start_date: date, end_date: date) -> int:
    delta = end_date - start_date
    return delta.days // 365

if __name__ == '__main__':
    start = date(2000, 1, 1)
    end = date(2023, 10, 15)
    result = calculate_year_difference(start, end)
    print(result)