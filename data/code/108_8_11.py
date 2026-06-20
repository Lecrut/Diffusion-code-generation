from dateutil import parser

def extract_day(date_str):
    dt = parser.parse(date_str)
    return dt.day

if __name__ == '__main__':
    sample_date_str = "2023-11-05T18:45:00"
    result = extract_day(sample_date_str)
    print(result)