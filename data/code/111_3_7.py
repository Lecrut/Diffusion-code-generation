from datetime import datetime, timedelta

def subtract_months(date_str, months):
    date_obj = datetime.strptime(date_str, "%B %d, %Y")
    new_date = date_obj - timedelta(days=months*30)
    return new_date.strftime("%B %d, %Y")

if __name__ == '__main__':
    result = subtract_months("October 15, 2023", 3)
    print(result)