def determine_outcome():
    a = 0b1010
    b = 0b1100
    c = 0b1110
    return (a & b) | (~c)

if __name__ == '__main__':
    print(determine_outcome())