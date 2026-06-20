from datetime import datetime

def format_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        return date_obj.strftime('%A, %B %d, %Y')
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."

if __name__ == '__main__':
    sample_date = '2023-10-05'
    print(format_date(sample_date))