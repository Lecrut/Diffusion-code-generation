from datetime import datetime

def convert_to_iso8601(date_string: str) -> str:
    dt = datetime.strptime(date_string, '%d-%m-%Y %H:%M:%S')
    return dt.isoformat()

if __name__ == '__main__':
    hardcoded_date = '25-12-2023 14:30:00'
    result = convert_to_iso8601(hardcoded_date)
    print(result)