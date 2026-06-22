def generate_multiplication_table_9():
    for i in range(1, 11):
        yield f"9 x {i} = {9 * i}"

if __name__ == '__main__':
    for row in generate_multiplication_table_9():
        print(row)