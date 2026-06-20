X = 10
Y = 20

def swap_values(a, b):
    return b, a

if __name__ == '__main__':
    print(f"Before swap: x={X}, y={Y}")
    X, Y = swap_values(X, Y)
    print(f"After swap: x={X}, y={Y}")