def perform_action(param):
    return f"Action performed with {param}"

if __name__ == '__main__':
    parameters = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
    results = [perform_action(p) for p in parameters.values()]
    print(results)