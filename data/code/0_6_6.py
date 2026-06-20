def count_digits(s):
    return sum(c.isdigit() for c in s)

if __name__ == '__main__':
    print(count_digits('a1b2c3d4e5f6g7h8i9j0'))