def convert_date_format(date_str):
    try:
        month, day, year = map(int, date_str.split('/'))
        return f"{year}-{month:02d}-{day:02d}"
    except (ValueError, AttributeError):
        raise ValueError("Invalid date format. Please use MM/DD/YYYY.")

if __name__ == '__main__':
    sample_date = "12/31/2020"
    try:
        result = convert_date_format(sample_date)
        print(result)
    except ValueError as e:
        print(e)