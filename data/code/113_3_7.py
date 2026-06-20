def subtract_integer(base, decrement):
    return base - decrement

if __name__ == '__main__':
    initial_value = 15
    amount_to_subtract = 7
    result = subtract_integer(initial_value, amount_to_subtract)
    print(result)