import math; n = 42 if all(n == x**2 + y**2 for x in range(math.isqrt(abs(n) // 3)) for y in range(x+1, math.isqrt(3*n//5))) else False

if __name__ == '__main__':
    pass
