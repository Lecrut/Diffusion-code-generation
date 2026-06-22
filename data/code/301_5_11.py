from datetime import datetime

def convert_date_format(date_str):
    try:
        dt_object = datetime.strptime(date_str, '%d/%m/%Y %I:%M %p')
        formatted_date = dt_object.strftime('%Y-%m-%dT%H:%M:00')
        return formatted_date
    except ValueError:
        raise ValueError("Invalid date format. Please use 'DD/MM/YYYY HH:MM AM/PM'.")

if __name__ == '__main__':
    sample_date = "15/08/2023 04:30 PM"
    try:
        result = convert_date_format(sample_date)
        print(result)
    except ValueError as e:
        print(e)