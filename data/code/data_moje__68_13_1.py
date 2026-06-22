def dollar_to_cents(dollar_amount):
    if dollar_amount < 0:
        return -round(abs(dollar_amount) * 100)
    return round(dollar_amount * 100)

if __name__ == '__main__':
    amount_1 = 10.50
    amount_2 = -25.75
    amount_3 = 0.01
    
    result_1 = dollar_to_cents(amount_1)
    result_2 = dollar_to_cents(amount_2)
    result_3 = dollar_to_cents(amount_3)
    
    print(result_1)
    print(result_2)
    print(result_3)