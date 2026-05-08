from datetime import date
if __name__ == '__main__':
    d = date(2023, 10, 25)
    print(d.weekday() < 5)