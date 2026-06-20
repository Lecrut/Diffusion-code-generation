from datetime import datetime, timedelta

def time_left_in_month(start_date_str, end_date_str):
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
    
    if start_date > end_date:
        raise ValueError("Start date must be before end date")
    
    days_in_month = (end_date - start_date).days + 1
    return timedelta(days=days_in_month)

if __name__ == '__main__':
    sample_start_date = '2023-04-15'
    sample_end_date = '2023-05-15'
    
    time_left = time_left_in_month(sample_start_date, sample_end_date)
    print(f"Time left in month: {time_left}")