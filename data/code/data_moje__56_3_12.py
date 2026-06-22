def multiplication_table():
    return [str(i) + " x 7 = " + str(i * 7) for i in range(1, 11)]

if __name__ == '__main__':
    result = multiplication_table()
    print(result)