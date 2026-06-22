def convert_date(date_str):
    parts = date_str.split('/')
    month = int(parts[0])
    day = int(parts[1])
    year = int(parts[2])
    if not (1 <= month <= 12 and 1 <= day <= 31 and year > 0):
        raise ValueError("Invalid date components")
    return f"{year:04d}-{month:02d}-{day:02d}"

if __name__ == '__main__':
    result = convert_date('12/31/2023')
    print(result)