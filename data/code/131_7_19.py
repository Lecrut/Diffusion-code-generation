NUM1 = 48
NUM2 = 18

def calculate_gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a
if __name__ == '__main__':
    result = calculate_gcd(NUM1, NUM2)
    print(result)