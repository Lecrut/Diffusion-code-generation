def extract_day(date_str):
    return date_str.split('-')[2]

if __name__ == '__main__':
    sample_date1 = '2023-04-01'
    result1 = extract_day(sample_date1)
    print(f"Date: {sample_date1}, Day of the month: {result1}")
    
    sample_date2 = '2023-12-31'
    result2 = extract_day(sample_date2)
    print(f"Date: {sample_date2}, Day of the month: {result2}")