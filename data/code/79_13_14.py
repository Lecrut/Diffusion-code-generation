import datetime

def calculate_next_month(start_date):
    try:
        if not isinstance(start_date, datetime.date):
            raise ValueError("Invalid input type. Please provide a datetime.date object.")
        
        next_month = start_date.replace(day=1) + datetime.timedelta(days=32)
        return next_month.replace(day=1)
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == '__main__':
    sample_start_date = datetime.date(2023, 1, 15)
    result = calculate_next_month(sample_start_date)
    if result:
        print(result.strftime('%Y-%m-%d'))