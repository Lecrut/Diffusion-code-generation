def fetch_penultimate(items):
    if len(items) < 2:
        raise ValueError("List must contain at least two elements")
    return items[-2]

if __name__ == '__main__':
    data_set = ["alpha", "beta", "gamma", "delta", "epsilon"]
    value = fetch_penultimate(data_set)
    print(value)