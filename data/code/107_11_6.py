def convert_date_format(date_str):
    month, day, year = date_str.split('/')
    return f"{year}-{month}-{day}"

if __name__ == '__main__':
    sample_date = "10/27/2023"
    result = convert_date_format(sample_date)
    print(result)