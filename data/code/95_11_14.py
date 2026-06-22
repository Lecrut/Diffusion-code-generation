def validate_triplet(a, b, c):
    def is_valid(n):
        return n > 0 and n < 100 and n % 2 == 0
    return is_valid(a) and is_valid(b) and is_valid(c)

if __name__ == '__main__':
    print(validate_triplet(2, 4, 6))
    print(validate_triplet(2, 4, 102))
    print(validate_triplet(2, 3, 4))
    print(validate_triplet(-2, 4, 6))
    print(validate_triplet(0, 2, 4))
    print(validate_triplet(100, 2, 4))
    print(validate_triplet(1, 2, 4))
    print(validate_triplet(2, 4, 5))