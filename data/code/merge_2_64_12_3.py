from datetime import date
def format_date(date_obj: date) -> str:
    return f"{date_obj.strftime('%B %d, %Y')}"
if __name__ == '__main__':
    sample_date = date(2023, 10, 5)
    print(format_date(sample_date))