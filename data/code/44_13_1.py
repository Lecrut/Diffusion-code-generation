def calculate_perimeter(L, W):
    return 2 * (L + W)
if __name__ == '__main__':
    L_sample = 10
    W_sample = 5
    perimeter = calculate_perimeter(L_sample, W_sample)
    print(perimeter)