import datetime
def process_date(date_str):
    try:
        day, month, year = map(int, date_str.split('-'))
        date_obj = datetime.date(year, month, day)
        day_of_week = date_obj.strftime("%A")
        print(f"Date: {date_obj.strftime('%d-%m-%Y')}")
        print(f"Day of the week: {day_of_week}")
    except ValueError:
        print("Error: Invalid date components or format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
if __name__ == '__main__':
    sample_date = "25-12-2023"
    process_date(sample_date)