from datetime import datetime
def convert_date_format(date_string):
    try:
        dt_object = datetime.strptime(date_string, '%d %B %Y')
        return dt_object.strftime('%Y-%m-%d')
    except ValueError:
        return "Invalid date format"
if __name__ == '__main__':
    sample1 = '27 October 2023'
    result1 = convert_date_format(sample1)
    print(result1)
    sample2 = '01 January 2024'
    result2 = convert_date_format(sample2)
    print(result2)
    sample3 = '31 December 2022'
    result3 = convert_date_format(sample3)
    print(result3)