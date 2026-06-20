from datetime import datetime

def format_custom_date():
    dt = datetime(2024, 1, 1, 12, 0, 0)
    formatted_dt = dt.strftime('%Y-%m-%d %I:%M %p')
    return formatted_dt

if __name__ == '__main__':
    result = format_custom_date()
    print(result)