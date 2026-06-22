def sort_descending(a, b, c):
    if not all(isinstance(i, (int, float)) for i in [a, b, c]):
        raise ValueError("All inputs must be numbers")
    return tuple(sorted([a, b, c], reverse=True))

if __name__ == '__main__':
    result = sort_descending(3.5, 1, 2)
    print(result)