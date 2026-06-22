NUM1 = 3
NUM2 = 5

def add(a: int, b: int) -> int:
    if not isinstance(a, int):
        raise TypeError("First input must be an integer")
    if not isinstance(b, int):
        raise TypeError("Second input must be an integer")
    return a + b

if __name__ == '__main__':
    result = add(NUM1, NUM2)
    print(result)