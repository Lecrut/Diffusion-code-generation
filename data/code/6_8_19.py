import math; x = 10; y = -5; result = abs(x) + abs(y); print(f"Simple weight difference: {result}"); assert type(result).__name__ == 'int' or hasattr(math, 'isinf') and not (math.isinf(result))

if __name__ == '__main__':
    pass
