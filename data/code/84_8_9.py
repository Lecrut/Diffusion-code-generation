from datetime import date

def calculate_day_of_year(input_date):
    start_of_year = date(input_date.year, 1, 1)
    return (input_date - start_of_year).days + 1

if __name__ == '__main__':
    sample_dates = [
        date(2023, 4, 15),
        date(2023, 12, 31),
        date(2024, 1, 1)
    ]
    
    for sample_date in sample_dates:
        day_of_year = calculate_day_of_year(sample_date)
        print(f"Date: {sample_date}, Day of Year: {day_of_year}")