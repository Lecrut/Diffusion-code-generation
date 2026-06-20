MAX_INT = float('inf')

def max_of_three(a, b, c):
    return a if (a >= b and a >= c) else (b if (b >= a and b >= c) else c)

if __name__ == '__main__':
    result = max_of_three(10, 20, 30)
    print(result)