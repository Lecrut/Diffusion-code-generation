def validate_input(a, b, c):
    return (a > 0) & (a % 2 == 0) & (a < 100) & \
           (b > 0) & (b % 2 == 0) & (b < 100) & \
           (c > 0) & (c % 2 == 0) & (c < 100)

if __name__ == '__main__':
    sample_values = (4, 68, 98)
    print(validate_input(*sample_values))