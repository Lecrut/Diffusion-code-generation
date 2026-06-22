def convert_dollars_to_cents(dollars_list):
    return [int(d * 100) for d in dollars_list]

if __name__ == '__main__':
    values = [10.50, 20.75, 30.00, 45.99]
    result = convert_dollars_to_cents(values)
    print(result)