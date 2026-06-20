from datetime import date

def get_day_of_month():
    return date(2024, 10, 10).day

if __name__ == '__main__':
    print(get_day_of_month())