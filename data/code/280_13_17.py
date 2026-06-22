def perform_action(param):
    return f"Action performed with {param}"

def validate_parameters(params):
    if not all(isinstance(p, int) for p in params):
        raise ValueError("All parameters must be integers")
    if len(params) != 5:
        raise ValueError("There must be exactly five parameters")

if __name__ == '__main__':
    parameters = [10, 20, 30, 40, 50]
    validate_parameters(parameters)
    results = [perform_action(p) for p in parameters]
    print(results)