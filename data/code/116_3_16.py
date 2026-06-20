NUM1 = 10
NUM2 = 20
NUM3 = 30

def sum_three_numbers(a=NUM1, b=NUM2, c=NUM3):
    return a + b + c

if __name__ == '__main__':
    result = sum_three_numbers()
    print(result)