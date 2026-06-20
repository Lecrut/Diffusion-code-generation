from decimal import Decimal, getcontext

def divide_decimals():
    getcontext().prec = 50
    num1 = Decimal('2.7182818284590452353602874713526624977572470936999')
    num2 = Decimal('3.1415926535897932384626433832795028841971693993751')
    result = num1 / num2
    return result

if __name__ == '__main__':
    print(divide_decimals())