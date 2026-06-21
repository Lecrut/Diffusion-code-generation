a = 10
b = 20
c = 30

def find_largest(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z

if __name__ == '__main__':
    largest = find_largest(a, b, c)
    print(largest)