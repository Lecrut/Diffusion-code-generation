from datetime import date

def get_next_15th():
    ref = date(2023, 3, 3)
    next_month = ref.month + 1
    next_year = ref.year
    if next_month > 12:
        next_month = 1
        next_year += 1
    return date(next_year, next_month, 15)

if __name__ == '__main__':
    print(get_next_15th())