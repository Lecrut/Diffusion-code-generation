NUM1 = 10
NUM2 = 20
NUM3 = 30

def sum_three(a, b, c):
    return sum((a, b, c))

if __name__ == '__main__':
    result = sum_three(NUM1, NUM2, NUM3)
    print(result)