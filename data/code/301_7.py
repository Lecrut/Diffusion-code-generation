from datetime import datetime
def convert_date_format(date_string):
    try:
        date_object = datetime.strptime(date_string, '%d %B %Y')
        return date_object.strftime('%Y-%m-%d')
    except ValueError:
        return "Invalid date format"
if __name__ == '__main__':
    sample_date1 = '27 October 2023'
    result1 = convert_date_format(sample_date1)
    print(f"{sample_date1} -> {result1}")
    sample_date2 = '01 January 2024'
    result2 = convert_date_format(sample_date2)
    print(f"{sample_date2} -> {result2}")
    sample_date3 = '31 December 2023'
    result3 = convert_date_format(sample_date3)
    print(f"{sample_date3} -> {result3}")