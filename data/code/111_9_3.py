import datetime
def extract_date_components(date_obj):
    return {
        "year": date_obj.year,
        "month": date_obj.month,
        "day": date_obj.day
    }
if __name__ == '__main__':
    sample_date_str = "2023-10-27"
    date_object = datetime.datetime.strptime(sample_date_str, "%Y-%m-%d").date()
    result = extract_date_components(date_object)
    print(result)