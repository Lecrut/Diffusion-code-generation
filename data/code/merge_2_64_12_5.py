from datetime import date
def format_date_with_full_month_name(date_obj: date) -> str:
    return date_obj.strftime("%B %d, %Y")
if __name__ == '__main__':
    sample_date = date(2023, 10, 5)
    result = format_date_with_full_month_name(sample_date)
    print(result)