def perform_operation(param):
    return f"Operation performed with {param}"

def validate_parameters(params):
    if not all(isinstance(p, int) for p in params):
        raise ValueError("All parameters must be integers")
    if len(params) != 5:
        raise ValueError("There must be exactly five parameters")

if __name__ == '__main__':
    sample_params = [10, 20, 30, 40, 50]
    validate_parameters(sample_params)
    results = [perform_operation(p) for p in sample_params]
    print(results)