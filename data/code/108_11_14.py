def get_day_of_month():
    from datetime import date
    d = date(2023, 3, 15)
    return d.day

if __name__ == '__main__':
    print(get_day_of_month())