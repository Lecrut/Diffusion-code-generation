def convert_dollars_to_cents(dollars):
    return int(dollars * 100)

if __name__ == '__main__':
    print(convert_dollars_to_cents(1.23))
    print(convert_dollars_to_cents(-1.23))
    print(convert_dollars_to_cents(0.0))