def get_first_and_last(items):
    if not items:
        raise ValueError("Input list cannot be empty")
    return items[0], items[-1]

if __name__ == '__main__':
    data = ["alpha", "beta", "gamma", "delta"]
    first, last = get_first_and_last(data)
    print(first)
    print(last)