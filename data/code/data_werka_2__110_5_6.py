from datetime import datetime

def sort_dates(date_strings):
    if not date_strings:
        return []
    def to_dt(ds):
        return datetime.strptime(ds, '%d/%m/%Y')
    return sorted(date_strings, key=to_dt)

if __name__ == '__main__':
    sample_dates = ['25/12/2023', '01/01/2024', '15/06/2023', '31/12/2022']
    sorted_dates = sort_dates(sample_dates)
    print(sorted_dates)