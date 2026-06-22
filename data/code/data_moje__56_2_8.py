OPERATION_NAMES = {
    "multiply": "x",
    "times": "*",
    "of": "·"
}

def generate_multiplication_table(n, op_name="multiply", limit=12):
    symbol = OPERATION_NAMES.get(op_name, "x")
    for i in range(1, limit + 1):
        result = n * i
        yield f"{n} {symbol} {i} = {result}"

if __name__ == '__main__':
    target_number = 9
    operation_type = "times"
    for line in generate_multiplication_table(target_number, operation_type):
        print(line)