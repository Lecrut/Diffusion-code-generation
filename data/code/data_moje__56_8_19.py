def get_six_multiplication_table():
    return {multiplier: 6 * multiplier for multiplier in range(1, 11)}

if __name__ == '__main__':
    result = get_six_multiplication_table()
    print(result)