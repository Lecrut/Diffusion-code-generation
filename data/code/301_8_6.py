from datetime import datetime
def format_date(date_obj, format_string):
    return date_obj.strftime(format_string)
if __name__ == '__main__':
    date_to_format = datetime(2023, 10, 27)
    format1 = '%d/%m/%Y'
    formatted1 = format_date(date_to_format, format1)
    print(f"Original Date: {date_to_format}")
    print(f"Format '{format1}': {formatted1}")
    format2 = '%B %d, %Y'
    formatted2 = format_date(date_to_format, format2)
    print(f"Format '{format2}': {formatted2}")
    format3 = '%Y-%m-%d %H:%M:%S'
    formatted3 = format_date(date_to_format, format3)
    print(f"Format '{format3}': {formatted3}")
    date_another = datetime(2024, 1, 5)
    format4 = '%m/%d/%y'
    formatted4 = format_date(date_another, format4)
    print(f"\nOriginal Date: {date_another}")
    print(f"Format '{format4}': {formatted4}")