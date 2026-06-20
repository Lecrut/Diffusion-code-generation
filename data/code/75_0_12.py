import datetime

def calculate_date_difference(date_string1, date_string2):
    formats = [
        "%Y-%m-%d",
        "%m/%d/%Y",
        "%d-%m-%Y",
        "%Y/%m/%d"
    ]
    
    def parse_date(date_str):
        for fmt in formats:
            try:
                return datetime.datetime.strptime(date_str, fmt).date()
            except ValueError:
                continue
        raise ValueError("Date format not recognized")
    
    date1 = parse_date(date_string1)
    date2 = parse_date(date_string2)
    
    return abs((date1 - date2).days)

if __name__ == '__main__':
    sample_date1 = "2023-04-15"
    sample_date2 = "15/04/2023"
    print(calculate_date_difference(sample_date1, sample_date2))