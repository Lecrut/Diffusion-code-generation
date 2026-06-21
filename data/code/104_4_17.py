from datetime import date

def is_same_date_tuple(d1, d2):
    try:
        dt1 = date(*d1)
        dt2 = date(*d2)
    except (TypeError, ValueError) as exc:
        raise ValueError("Invalid date tuple format") from exc
    return dt1 == dt2

if __name__ == '__main__':
    first = (2024, 2, 29)
    second = (2024, 2, 28)
    output = is_same_date_tuple(first, second)
    print(output)