from datetime import date

if __name__ == '__main__':
    DATE_A = date(2023, 10, 26)
    DATE_B = date(2023, 10, 26)
    DATE_C = date(2023, 10, 27)

    result = DATE_A == DATE_B
    print(result)