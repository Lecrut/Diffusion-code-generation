from numbers import Number
def is_positive(value: Number) -> bool:
    return value > 0
if __name__ == '__main__':
    print(is_positive(5))             
    print(is_positive(-3))             
    print(is_positive(0.0))            
    print(is_positive(1e-10))