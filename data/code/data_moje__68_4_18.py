def convert_dollars_to_cents(dollars):
    return int(dollars * 100)

if __name__ == '__main__':
    result = convert_dollars_to_cents(12.34)
    print(result)