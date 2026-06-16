from datetime import date
def format_date(date_obj):
    return date_obj.strftime('%B %d, %Y')
if __name__ == '__main__':
    sample_date = date(2023, 1, 1)
    formatted_string = format_date(sample_date)
    print(formatted_string)
    sample_date_2 = date(2024, 5, 15)
    formatted_string_2 = format_date(sample_date_2)
    print(formatted_string_2)