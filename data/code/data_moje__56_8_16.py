def get_multiplication_table_of_6():
    result = {}
    for i in range(1, 11):
        result[i] = 6 * i
    return result

if __name__ == '__main__':
    print(get_multiplication_table_of_6())