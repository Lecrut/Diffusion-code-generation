from datetime import datetime

def sort_date_strings(date_strings):
    def parse_date(date_str):
        return datetime.strptime(date_str, '%m-%d-%Y')
    
    sorted_dates = sorted(date_strings, key=parse_date)
    return sorted_dates

if __name__ == '__main__':
    sample_dates = ['12-31-2023', '01-01-2023', '06-15-2022', '03-10-2023']
    result = sort_date_strings(sample_dates)
    print(result)