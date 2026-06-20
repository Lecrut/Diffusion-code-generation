X = 10
Y = 20

def reverse_numbers(a, b):
    while a != 0:
        temp = a
        a = b - b // a * a
        b = temp
    return b
if __name__ == '__main__':
    print(f'x: {X}, y: {Y}')
    X, Y = reverse_numbers(X, Y)
    print(f'Reversed x: {X}, Reversed y: {Y}')