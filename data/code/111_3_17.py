from datetime import datetime, timedelta

def subtract_three_months(date_str):
    date_obj = datetime.strptime(date_str, "%B %d, %Y")
    new_date_obj = date_obj - timedelta(days=3*30)
    return new_date_obj.strftime("%B %d, %Y")

if __name__ == '__main__':
    sample_date = "October 15, 2023"
    result = subtract_three_months(sample_date)
    print(result)