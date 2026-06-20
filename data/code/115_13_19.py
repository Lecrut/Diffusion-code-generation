from decimal import Decimal, getcontext

def perform_division():
    getcontext().prec = 50
    dividend = Decimal('27182818284590452353602874713526624977572470936999')
    divisor = Decimal('314159265358979323846264338327950288419716939937510')
    result = dividend / divisor
    return result

if __name__ == '__main__':
    division_result = perform_division()
    print(division_result)