def bitwise_operations(flag1, flag2):
    return (flag1 & flag2), (flag1 | flag2), (~flag1)

if __name__ == '__main__':
    result_and, result_or, result_not = bitwise_operations(5, 3)
    print(f"AND: {result_and}, OR: {result_or}, NOT: {result_not}")