from datetime import datetime

def dates_in_same_week(date1_str, date2_str):
    date_format = '%Y-%m-%d'
    date1 = datetime.strptime(date1_str, date_format)
    date2 = datetime.strptime(date2_str, date_format)
    return date1.isocalendar()[1] == date2.isocalendar()[1]

if __name__ == '__main__':
    sample_date1 = "2023-04-01"
    sample_date2 = "2023-04-07"
    result1 = dates_in_same_week(sample_date1, sample_date2)
    print(f"{sample_date1} and {sample_date2} are in the same week: {result1}")
    
    sample_date1 = "2023-04-01"
    sample_date2 = "2023-04-08"
    result2 = dates_in_same_week(sample_date1, sample_date2)
    print(f"{sample_date1} and {sample_date2} are in the same week: {result2}")
    
    sample_date1 = "2023-04-07"
    sample_date2 = "2023-04-08"
    result3 = dates_in_same_week(sample_date1, sample_date2)
    print(f"{sample_date1} and {sample_date2} are in the same week: {result3}")