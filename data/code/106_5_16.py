from datetime import date

def calculate_year_difference(start_date: date, end_date: date) -> int:
    return end_date.year - start_date.year

if __name__ == '__main__':
    start = date(2010, 5, 15)
    end = date(2023, 10, 20)
    result = calculate_year_difference(start, end)
    print(result)