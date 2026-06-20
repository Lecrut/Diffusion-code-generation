def determine_outcome(a, b, c):
    return (a & b) | (~c)

if __name__ == '__main__':
    print(determine_outcome(1, 2, 3))