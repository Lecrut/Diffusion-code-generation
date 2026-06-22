from datetime import datetime

def convert_date_format(date_str):
    dt_object = datetime.strptime(date_str, '%d/%m/%Y %I:%M %p')
    formatted_date = dt_object.strftime('%Y-%m-%dT%H:%M:00')
    return formatted_date

if __name__ == '__main__':
    sample_date = "15/08/2023 04:30 PM"
    converted_date = convert_date_format(sample_date)
    print(converted_date)