AND_FLAG = 1
OR_FLAG = 2
NOT_FLAG = 4

def apply_flag_operations(a: int, b: int, flag: int) -> int:
    if flag == AND_FLAG:
        return a & b
    elif flag == OR_FLAG:
        return a | b
    elif flag == NOT_FLAG:
        return ~a
    else:
        raise ValueError("Invalid flag")

if __name__ == '__main__':
    result_and = apply_flag_operations(5, 3, AND_FLAG)
    result_or = apply_flag_operations(5, 3, OR_FLAG)
    result_not_a = apply_flag_operations(5, 3, NOT_FLAG)
    print(f"AND: {result_and}, OR: {result_or}, NOT(a): {result_not_a}")