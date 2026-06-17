from datetime import datetime
def format_date(date_obj, format_string):
    return date_obj.strftime(format_string)
if __name__ == '__main__':
    date1 = datetime(2023, 10, 27)
    date2 = datetime(2024, 1, 5)
    print("--- Date Formatting Examples ---")
    format_str1 = '%d/%m/%Y'
    formatted_date1_1 = format_date(date1, format_str1)
    print(f"Date: {date1}, Format: '{format_str1}' -> Output: {formatted_date1_1}")
    format_str2 = '%B %d, %Y'
    formatted_date1_2 = format_date(date1, format_str2)
    print(f"Date: {date1}, Format: '{format_str2}' -> Output: {formatted_date1_2}")
    format_str3 = '%Y-%m-%d'
    formatted_date2_1 = format_date(date2, format_str3)
    print(f"Date: {date2}, Format: '{format_str3}' -> Output: {formatted_date2_1}")
    format_str4 = '%m/%d/%Y'
    formatted_date1_3 = format_date(date1, format_str4)
    print(f"Date: {date1}, Format: '{format_str4}' -> Output: {formatted_date1_3}")
    format_str5 = '%B %d, %Y'
    formatted_date2_2 = format_date(date2, format_str5)
    print(f"Date: {date2}, Format: '{format_str5}' -> Output: {formatted_date2_2}")