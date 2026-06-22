def sort_descending(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numeric")
    if a < b:
        return (b, a)
    return (a, b)

if __name__ == '__main__':
    result = sort_descending(10, 20)
    print(result)