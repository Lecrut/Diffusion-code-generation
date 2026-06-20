from datetime import datetime

def format_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        return date_obj.strftime('%d/%m/%Y')
    except ValueError:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")

if __name__ == '__main__':
    sample_date = '2023-10-05'
    try:
        formatted_date = format_date(sample_date)
        print(formatted_date)
    except ValueError as e:
        print(e)