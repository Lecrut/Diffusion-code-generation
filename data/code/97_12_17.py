def xor_operation(val1, val2):
    return val1 ^ val2

def generate_truth_table():
    values = [0, 1]
    for v1 in values:
        for v2 in values:
            result = xor_operation(v1, v2)
            print(f"{v1} XOR {v2} = {result}")

if __name__ == '__main__':
    generate_truth_table()