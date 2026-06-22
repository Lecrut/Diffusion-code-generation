def get_later_iso_date(d1: str, d2: str) -> str:
    y1, m1, d_val1 = [int(p) for p in d1.split('-')]
    y2, m2, d_val2 = [int(p) for p in d2.split('-')]
    if y1 != y2:
        return d1 if y1 > y2 else d2
    if m1 != m2:
        return d1 if m1 > m2 else d2
    return d1 if d_val1 >= d_val2 else d2

if __name__ == '__main__':
    print(get_later_iso_date("2024-01-30", "2024-01-31"))