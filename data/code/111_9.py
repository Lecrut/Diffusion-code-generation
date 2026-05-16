import datetime
def extract_date_components(date_str):
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    return {
        "year": date_obj.year,
        "month": date_obj.month,
        "day": date_obj.day
    }
if __name__ == '__main__':
    sample_date = "2023-10-27"
    result = extract_date_components(sample_date)
    print(result)