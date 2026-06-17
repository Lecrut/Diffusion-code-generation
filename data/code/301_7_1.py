from datetime import datetime
def convert_date_format(date_string):
    try:
        date_object = datetime.strptime(date_string, '%d %B %Y')
        return date_object.strftime('%Y-%m-%d')
    except ValueError:
        return "Error: Invalid date format"
if __name__ == '__main__':
    sample_date1 = '27 October 2023'
    sample_date2 = '1 January 2024'
    sample_date3 = '5 March 1999'
    result1 = convert_date_format(sample_date1)
    result2 = convert_date_format(sample_date2)
    result3 = convert_date_format(sample_date3)
    print(f"Input: {sample_date1}, Output: {result1}")
    print(f"Input: {sample_date2}, Output: {result2}")
    print(f"Input: {sample_date3}, Output: {result3}")