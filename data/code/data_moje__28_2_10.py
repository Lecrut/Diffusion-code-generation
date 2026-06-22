def sort_pair(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("Inputs must be numeric")
    if x < y:
        return (x, y)
    return (y, x)

if __name__ == '__main__':
    output = sort_pair(10, 20)
    print(output)
    output = sort_pair(20, 10)
    print(output)
    output = sort_pair(-5, -10)
    print(output)
    try:
        sort_pair(1, "2")
    except TypeError as e:
        print(e)