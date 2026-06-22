def multiplication_table_six():
    return {multiplier: 6 * multiplier for multiplier in range(1, 11)}

if __name__ == '__main__':
    print(multiplication_table_six())