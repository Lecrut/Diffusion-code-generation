from dateutil import parser

def extract_day(date_string):
    try:
        date = parser.parse(date_string)
        return date.day
    except ValueError:
        raise ValueError("Invalid date format")

if __name__ == '__main__':
    sample_date_string = "2023-10-27T14:30:00"
    result = extract_day(sample_date_string)
    print(result)