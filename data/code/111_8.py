from datetime import date
if __name__ == '__main__':
    date_list = [date(2023, 10, 26), date(2024, 1, 15), date(2022, 12, 31)]
    for dt in date_list:
        year = dt.year
        month = dt.month
        print(f"Year: {year}, Month: {month}")