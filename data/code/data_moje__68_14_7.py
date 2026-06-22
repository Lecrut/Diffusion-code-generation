def convert_dollars_to_cents(dollars):
    return int(dollars * 100)

if __name__ == '__main__':
    dollars_amount = 12.34
    result = convert_dollars_to_cents(dollars_amount)
    print(result)