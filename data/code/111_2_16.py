import datetime

def get_day_of_week(year, month, day):
    date = datetime.date(year, month, day)
    return date.strftime('%A')

if __name__ == '__main__':
    sample_year = 2024
    sample_month = 2
    sample_day = 29
    
    result = get_day_of_week(sample_year, sample_month, sample_day)
    print(f"Day of the week for {sample_month}/{sample_day}/{sample_year}: {result}")