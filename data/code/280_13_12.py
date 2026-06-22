def perform_operation(param):
    if not isinstance(param, int) or param < 1:
        raise ValueError("Parameter must be a positive integer")
    return f"Operation performed with {param}"

if __name__ == '__main__':
    parameters = [3, 6, 9, 12, 15]
    results = [perform_operation(p) for p in parameters]
    print(results)