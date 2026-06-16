def convert_dates():
    date_strings = ["01-15-2023", "12-31-2022", "05-20-2024"]
    for date_str in date_strings:
        month, day, year = date_str.split('-')
        formatted_date = f"{year}/{month}/{day}"
        print(formatted_date)
if __name__ == '__main__':
    convert_dates()