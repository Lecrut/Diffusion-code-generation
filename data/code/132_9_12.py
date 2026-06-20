def determine_outcome():
    a = 5
    b = 3
    c = 8
    return (a & b) | (~c)

if __name__ == '__main__':
    print(determine_outcome())