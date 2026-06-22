def get_multiplication_table(number):
    table = {}
    for multiplier in range(1, 11):
        table[multiplier] = number * multiplier
    return table

if __name__ == '__main__':
    result = get_multiplication_table(6)
    print(result)