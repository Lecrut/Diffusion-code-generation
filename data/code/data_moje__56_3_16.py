def generate_multiplication_table_seven():
    return [f"7 x {i} = {7 * i}" for i in range(1, 11)]

if __name__ == '__main__':
    result = generate_multiplication_table_seven()
    print(result)