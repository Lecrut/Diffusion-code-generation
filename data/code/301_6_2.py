def convert_dates(date_strings):
    converted_dates = []
    for date_str in date_strings:
        month, day, year = date_str.split('-')
        new_date = f"{year}/{month}/{day}"
        converted_dates.append(new_date)
    return converted_dates
if __name__ == '__main__':
    date_list = ["01-15-2023", "12-31-2022", "05-20-2024"]
    result = convert_dates(date_list)
    for date in result:
        print(date)