from datetime import date

def day_of_month(date_obj):
    return date_obj.day

if __name__ == '__main__':
    sample_date = date(2023, 9, 15)
    print(day_of_month(sample_date))