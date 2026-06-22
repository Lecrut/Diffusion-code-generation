from datetime import datetime

def date_to_string(date_obj):
    return date_obj.strftime('%A, %B %d, %Y')

if __name__ == '__main__':
    sample_date = datetime(2023, 12, 31)
    formatted_date = date_to_string(sample_date)
    print(f"Formatted Date: {formatted_date}")

    another_sample_date = datetime(2024, 6, 5)
    another_formatted_date = date_to_string(another_sample_date)
    print(f"Another Formatted Date: {another_formatted_date}")