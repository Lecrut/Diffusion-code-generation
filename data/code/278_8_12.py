from datetime import datetime

def format_dates(date_list):
    month_names = {
        1: 'January', 2: 'February', 3: 'March', 4: 'April',
        5: 'May', 6: 'June', 7: 'July', 8: 'August',
        9: 'September', 10: 'October', 11: 'November', 12: 'December'
    }
    
    for date_str in date_list:
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            month_name = month_names[date_obj.month]
            formatted_date = f"{month_name} {date_obj.day}, {date_obj.year}"
            print(formatted_date)
        except ValueError:
            print(f"Invalid date format: {date_str}")

if __name__ == '__main__':
    sample_dates = ['2023-01-01', '2023-12-25', '2024-07-04']
    format_dates(sample_dates)