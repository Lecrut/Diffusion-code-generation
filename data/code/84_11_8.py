import datetime

def calculate_day_of_year(year, month, day):
    return (datetime.date(year, month, day) - datetime.date(year, 1, 1)).days + 1

if __name__ == '__main__':
    print(f"Day of year for 2024-03-15: {calculate_day_of_year(2024, 3, 15)}")
    print(f"Day of year for 2000-01-01: {calculate_day_of_year(2000, 1, 1)}")
    print(f"Day of year for 2023-12-31: {calculate_day_of_year(2023, 12, 31)}")
    print(f"Day of year for 2024-02-29: {calculate_day_of_year(2024, 2, 29)}")
    print(f"Day of year for 2023-01-01: {calculate_day_of_year(2023, 1, 1)}")