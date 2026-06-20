def bitwise_operations(a: int, b: int) -> tuple:
    return a & b, a | b, ~a

if __name__ == '__main__':
    result_and, result_or, result_not = bitwise_operations(5, 3)
    print(f"AND: {result_and}, OR: {result_or}, NOT: {result_not}")