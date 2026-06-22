def multiplication_table_of_9():
    return [f"{i} x 9 = {i * 9}" for i in range(1, 11)]

if __name__ == '__main__':
    result = multiplication_table_of_9()
    print(result)