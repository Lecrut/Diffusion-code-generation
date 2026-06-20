def xor_table():
    inputs = [0, 1]
    for x in inputs:
        for y in inputs:
            result = x ^ y
            print(f"{x} XOR {y} = {result}")

if __name__ == '__main__':
    xor_table()