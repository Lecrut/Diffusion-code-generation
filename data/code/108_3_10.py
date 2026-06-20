def extract_day(date_str):
    return int(date_str.split('-')[2])

if __name__ == '__main__':
    sample_date1 = '2023-04-01'
    result1 = extract_day(sample_date1)
    print(f"Date: {sample_date1}, Day: {result1}")
    
    sample_date2 = '2023-12-25'
    result2 = extract_day(sample_date2)
    print(f"Date: {sample_date2}, Day: {result2}")