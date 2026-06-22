from datetime import datetime

def date_range(date_list):
    if not date_list:
        return None
    start_date = min(date_list, key=lambda x: datetime.strptime(x, '%Y-%m-%d'))
    end_date = max(date_list, key=lambda x: datetime.strptime(x, '%Y-%m-%d'))
    delta = (datetime.strptime(end_date, '%Y-%m-%d') - datetime.strptime(start_date, '%Y-%m-%d')).days
    return start_date, end_date, delta

if __name__ == '__main__':
    sample_dates1 = ['2023-01-01', '2023-02-01', '2023-03-01']
    result1 = date_range(sample_dates1)
    print(f"Range for {sample_dates1}: Start Date - {result1[0]}, End Date - {result1[1]}, Days Difference - {result1[2]}")
    
    sample_dates2 = ['2022-12-31', '2023-04-30']
    result2 = date_range(sample_dates2)
    print(f"Range for {sample_dates2}: Start Date - {result2[0]}, End Date - {result2[1]}, Days Difference - {result2[2]}")