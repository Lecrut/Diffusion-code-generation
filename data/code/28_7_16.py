def sort_descending(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numeric")
    if a > b:
        return (a, b)
    else:
        return (b, a)

if __name__ == '__main__':
    result = sort_descending(3, 7)
    print(result)
    result2 = sort_descending(10.5, 2.3)
    print(result2)
    result3 = sort_descending(-5, -1)
    print(result3)