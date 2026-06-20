def determine_outcome(a, b, c):
    return (a & b) | (~c)

if __name__ == '__main__':
    val1 = True
    val2 = False
    val3 = True
    result = determine_outcome(val1, val2, val3)
    print(result)