from datetime import datetime
def format_date(date_obj, format_string):
    return date_obj.strftime(format_string)
if __name__ == '__main__':
    date1 = datetime(2023, 10, 27)
    date2 = datetime(2024, 1, 5)
    print("--- Date Formatting Examples ---")
    format_str1 = '%d/%m/%Y'
    formatted1 = format_date(date1, format_str1)
    print(f"Date {date1.date()} formatted as '{format_str1}': {formatted1}")
    format_str2 = '%B %d, %Y'
    formatted2 = format_date(date1, format_str2)
    print(f"Date {date1.date()} formatted as '{format_str2}': {formatted2}")
    format_str3 = '%Y-%m-%d'
    formatted3 = format_date(date1, format_str3)
    print(f"Date {date1.date()} formatted as '{format_str3}': {formatted3}")
    print("\n" + "="*30 + "\n")
    print("--- Second Date Object Examples ---")
    format_str4 = '%m/%d/%Y'
    formatted4 = format_date(date2, format_str4)
    print(f"Date {date2.date()} formatted as '{format_str4}': {formatted4}")
    format_str5 = '%B %Y'
    formatted5 = format_date(date2, format_str5)
    print(f"Date {date2.date()} formatted as '{format_str5}': {formatted5}")