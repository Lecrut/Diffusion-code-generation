NUM1 = 10
NUM2 = 5

def add_quantities(a: int = NUM1, b: int = NUM2) -> int:
    return a + b

if __name__ == '__main__':
    result = add_quantities()
    print(result)