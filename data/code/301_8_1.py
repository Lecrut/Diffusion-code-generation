from datetime import datetime
def format_date(date_obj, format_string):
    return date_obj.strftime(format_string)
if __name__ == '__main__':
    date1 = datetime(2023, 10, 27)
    date2 = datetime(2024, 1, 5)
    format_a = '%d/%m/%Y'
    formatted_a1 = format_date(date1, format_a)
    formatted_a2 = format_date(date2, format_a)
    format_b = '%B %d, %Y'
    formatted_b1 = format_date(date1, format_b)
    formatted_b2 = format_date(date2, format_b)
    print(f"Date 1: {date1}")
    print(f"Format '{format_a}': {formatted_a1}")
    print(f"Format '{format_b}': {formatted_b1}")
    print("-" * 20)
    print(f"Date 2: {date2}")
    print(f"Format '{format_a}': {formatted_a2}")
    print(f"Format '{format_b}': {formatted_b2}")