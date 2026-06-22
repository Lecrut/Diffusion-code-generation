def get_seven_multiplication_table():
    return [f"7 x {i} = {7 * i}" for i in range(1, 11)]

if __name__ == '__main__':
    print(get_seven_multiplication_table())