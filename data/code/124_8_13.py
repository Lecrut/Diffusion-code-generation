def bitwise_add(a, b):
    while b:
        carry = a & b
        a ^= b
        b = carry << 1
    return a

def standard_add(a, b):
    return a + b

def add_using_conditions(a, b):
    if a >= 0 and b >= 0:
        return bitwise_add(a, b)
    else:
        return standard_add(a, b)

if __name__ == '__main__':
    result = (add_using_conditions(10, 5), add_using_conditions(-3, -2))
    print(result)