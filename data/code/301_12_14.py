from datetime import datetime

def format_datetime(date_obj):
    return date_obj.strftime('%A, %B %d, %Y')

if __name__ == '__main__':
    sample_date = datetime(2023, 12, 31)
    formatted_date = format_datetime(sample_date)
    print(f"Formatted Date: {formatted_date}")
    
    sample_date_2 = datetime(2024, 6, 5)
    formatted_date_2 = format_datetime(sample_date_2)
    print(f"Formatted Date: {formatted_date_2}")