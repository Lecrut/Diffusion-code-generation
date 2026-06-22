def convert_to_cents(dollars):
    return int(dollars * 100)

if __name__ == '__main__':
    positive_amount = 12.35
    negative_amount = -50.00
    zero_amount = 0.0
    print(convert_to_cents(positive_amount))
    print(convert_to_cents(negative_amount))
    print(convert_to_cents(zero_amount))