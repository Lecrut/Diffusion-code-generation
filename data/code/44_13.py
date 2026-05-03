def calculate_perimeter(L, W):
    return 2 * (L + W)
if __name__ == '__main__':
    L_val = 10
    W_val = 5
    perimeter = calculate_perimeter(L_val, W_val)
    print(perimeter)