def perform_action(param):
    if not isinstance(param, int) or param < 0:
        raise ValueError("Parameter must be a non-negative integer")
    return f"Action performed with {param}"

if __name__ == '__main__':
    parameters = [1, 2, 3, 4, 5]
    results = [perform_action(p) for p in parameters]
    print(results)