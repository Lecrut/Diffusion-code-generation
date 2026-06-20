SUM_CONSTANTS = (10, 20, 30)

def calculate_sum(a, b, c):
    return sum((a, b, c))

if __name__ == '__main__':
    result = calculate_sum(*SUM_CONSTANTS)
    print(result)