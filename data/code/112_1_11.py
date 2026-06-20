def add_two_numbers(a: float, b: float) -> float:
    return round(a + b, 15)

if __name__ == '__main__':
    NUM1 = 3.141592653589793
    NUM2 = 2.718281828459045
    result = add_two_numbers(NUM1, NUM2)
    print(result)