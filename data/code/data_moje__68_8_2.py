def dollar_to_cents(amount):
    return int(abs(amount * 100))

if __name__ == '__main__':
    result = dollar_to_cents(-5.5)
    print(result)