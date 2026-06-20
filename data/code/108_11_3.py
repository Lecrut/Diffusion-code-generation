from datetime import date

def get_day_of_month():
    return date(2023, 3, 15).day

if __name__ == '__main__':
    print(get_day_of_month())