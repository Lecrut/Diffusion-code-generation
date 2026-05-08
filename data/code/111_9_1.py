from datetime import date
def extract_date_components(date_obj):
    return {
        "year": date_obj.year,
        "month": date_obj.month,
        "day": date_obj.day
    }
if __name__ == '__main__':
    sample_date = date(2023, 10, 27)
    result = extract_date_components(sample_date)
    print(result)