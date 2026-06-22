def multiplication_table_6():
    result = {}
    for multiplier in range(1, 11):
        result[multiplier] = 6 * multiplier
    return result

if __name__ == '__main__':
    print(multiplication_table_6())