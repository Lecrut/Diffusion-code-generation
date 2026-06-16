import datetime
def convert_date_format(date_string):
    parts = date_string.split()
    day = int(parts[0])
    month_name = parts[1]
    year = int(parts[2])
    month_map = {
        'January': '01', 'February': '02', 'March': '03', 'April': '04',
        'May': '05', 'June': '06', 'July': '07', 'August': '08',
        'September': '09', 'October': '10', 'November': '11', 'December': '12'
    }
    month = month_map[month_name]
    return f"{year}-{month}-{day:02d}"
if __name__ == '__main__':
    sample_date1 = '27 October 2023'
    sample_date2 = '1 January 2024'
    sample_date3 = '5 March 1999'
    result1 = convert_date_format(sample_date1)
    result2 = convert_date_format(sample_date2)
    result3 = convert_date_format(sample_date3)
    print(result1)
    print(result2)
    print(result3)