def bitwise_add(a, b):
    while b != 0:
        carry = a & b
        a ^= b
        b = carry << 1
    return a

def arithmetic_operations():
    try:
        result_add = bitwise_add(10, 5)
        result_mul = 10 * 5
        result_div = 10 // 5
        result_mod = 10 % 5
        return (result_add, result_mul, result_div, result_mod)
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == '__main__':
    results = arithmetic_operations()
    if results is not None:
        print(results)