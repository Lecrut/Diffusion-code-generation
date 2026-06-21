def sort_pair(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numbers")
    pair = [a, b]
    pair.sort()
    return tuple(pair)

if __name__ == '__main__':
    first = 10
    second = -5
    outcome = sort_pair(first, second)
    print(outcome)