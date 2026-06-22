def get_multiplication_table_of_seven():
    return [f"{i} x 7 = {i * 7}" for i in range(1, 11)]

if __name__ == '__main__':
    result = get_multiplication_table_of_seven()
    print(result)