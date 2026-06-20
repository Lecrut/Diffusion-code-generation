BITWISE_AND = '&'
BITWISE_OR = '|'
BITWISE_NOT = '~'

def bitwise_operations(a: int, b: int) -> (int, int, int):
    and_result = a & b
    or_result = a | b
    not_a = ~a
    return and_result, or_result, not_a

if __name__ == '__main__':
    result_and, result_or, result_not = bitwise_operations(5, 3)
    print(f"AND: {result_and}, OR: {result_or}, NOT: {result_not}")