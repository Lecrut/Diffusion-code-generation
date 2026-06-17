from datetime import date
def format_date_explicit_month(date_obj: date) -> str:
    return date_obj.strftime("%B %d, %Y")
if __name__ == '__main__':
    sample_dates = [date(2023, 10, 5), date(2024, 6, 15)]
    for d in sample_dates:
        formatted_date = format_date_explicit_month(d)
        print(formatted_date)