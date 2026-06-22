def get_multiplication_table(base):
    return [base * i for i in range(1, 11)]

if __name__ == '__main__':
    result = get_multiplication_table(4)
    print(result)