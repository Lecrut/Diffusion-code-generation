from datetime import date

def calculate_year_difference(end_date: date, start_date: date) -> int:
    return abs((end_date.year - start_date.year))

if __name__ == '__main__':
    date1 = date(2023, 4, 15)
    date2 = date(1990, 7, 20)
    difference = calculate_year_difference(date1, date2)
    print(f"The difference between {date1.year} and {date2.year} is: {difference}")