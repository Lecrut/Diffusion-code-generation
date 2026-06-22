def dollar_to_cents(amount):
    return amount * 100

if __name__ == '__main__':
    positive_dollar = 12.50
    negative_dollar = -3.75
    zero_dollar = 0.00
    
    print(dollar_to_cents(positive_dollar))
    print(dollar_to_cents(negative_dollar))
    print(dollar_to_cents(zero_dollar))