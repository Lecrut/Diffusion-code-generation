def is_greater(a: float, b: float) -> bool:
    if a != a and b != b:                
        return False
    elif a == a and b == b:                  
        return a > b
    else:
        return True
if __name__ == '__main__':
    print(is_greater(5.0, 3.0))
    print(is_greater(float('nan'), float('nan')))
    print(is_greater(-1.0, -2.0))