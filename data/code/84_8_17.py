from datetime import date

def calculate_day_of_year(input_date):
    year_start = date(input_date.year, 1, 1)
    return (input_date - year_start).days + 1

if __name__ == '__main__':
    sample_date_1 = date(2023, 4, 15)
    day_of_year_1 = calculate_day_of_year(sample_date_1)
    print(f"Date: {sample_date_1}, Day of Year: {day_of_year_1}")

    sample_date_2 = date(2023, 12, 31)
    day_of_year_2 = calculate_day_of_year(sample_date_2)
    print(f"Date: {sample_date_2}, Day of Year: {day_of_year_2}")