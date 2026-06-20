A, B = 10, 20

if __name__ == '__main__':
    print(f"Before reversal: a={A}, b={B}")
    A, B = B, A
    print(f"After reversal: a={A}, b={B}")