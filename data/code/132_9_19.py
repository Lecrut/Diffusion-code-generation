def determine_outcome():
    a = 0b1101
    b = 0b1011
    c = 0b1110
    return (a & b) | (~c & a)

if __name__ == '__main__':
    print(determine_outcome())