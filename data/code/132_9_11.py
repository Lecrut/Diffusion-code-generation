def determine_outcome():
    a = True
    b = False
    c = True
    return (a & b) | (~c)

if __name__ == '__main__':
    print(determine_outcome())