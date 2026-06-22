def convert_date(date_str):
    components = date_str.split('/')
    month_value = int(components[0])
    day_value = int(components[1])
    year_value = int(components[2])
    if not (1 <= month_value <= 12):
        raise ValueError("Month out of range")
    if not (1 <= day_value <= 31):
        raise ValueError("Day out of range")
    if year_value < 1:
        raise ValueError("Year out of range")
    formatted_year = str(year_value).zfill(4)
    formatted_month = str(month_value).zfill(2)
    formatted_day = str(day_value).zfill(2)
    return f"{formatted_year}-{formatted_month}-{formatted_day}"

if __name__ == '__main__':
    sample_input = "07/04/2024"
    output = convert_date(sample_input)
    print(output)