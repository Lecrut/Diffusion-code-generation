def get_highest_value():
    a = 10.5
    b = 20.3
    c = 15.8
    if a >= b and a >= c:
        result = a
    elif b >= a and b >= c:
        result = b
    else:
        result = c
    return result

if __name__ == '__main__':
    print(get_highest_value())