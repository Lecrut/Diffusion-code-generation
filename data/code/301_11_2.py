from datetime import date
def format_date(date_obj):
    return date_obj.strftime("%B %d, %Y")
if __name__ == '__main__':
    sample_date = date(2023, 1, 1)
    formatted = format_date(sample_date)
    print(formatted)