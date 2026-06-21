from datetime import date

def same_week(d1: date, d2: date) -> bool:
    iso1 = d1.isocalendar()
    iso2 = d2.isocalendar()
    return iso1[:2] == iso2[:2]

if __name__ == '__main__':
    d1 = date(2023, 1, 1)
    d2 = date(2023, 1, 7)
    print(same_week(d1, d2))