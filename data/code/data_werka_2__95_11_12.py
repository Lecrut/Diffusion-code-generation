def validate_triplet_positive_even_under_hundred(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a % 2 != 0 or b % 2 != 0 or c % 2 != 0:
        return False
    if a >= 100 or b >= 100 or c >= 100:
        return False
    return True

if __name__ == '__main__':
    print(validate_triplet_positive_even_under_hundred(10, 20, 30))
    print(validate_triplet_positive_even_under_hundred(10, 20, 100))
    print(validate_triplet_positive_even_under_hundred(11, 20, 30))
    print(validate_triplet_positive_even_under_hundred(-10, 20, 30))
    print(validate_triplet_positive_even_under_hundred(0, 20, 30))