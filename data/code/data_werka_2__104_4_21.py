from datetime import date

def check_date_equality(first_date, second_date):
    y1, m1, d1 = first_date
    y2, m2, d2 = second_date
    dt1 = date(y1, m1, d1)
    dt2 = date(y2, m2, d2)
    return dt1 == dt2

if __name__ == '__main__':
    p1 = (2020, 1, 1)
    p2 = (2021, 1, 1)
    answer = check_date_equality(p1, p2)
    print(answer)