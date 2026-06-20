SUM_CONSTANTS = (10, 25, 40)

def calculate_three_sum(a, b, c):
    return a + b + c

if __name__ == '__main__':
    sample_values = SUM_CONSTANTS
    result = calculate_three_sum(*sample_values)
    print(result)