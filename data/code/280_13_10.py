MAX_ITERATIONS = 5

def perform_action(param):
    return f"Action performed with {param}"

if __name__ == '__main__':
    parameters = [1, 2, 3, 4, 5]
    results = [perform_action(p) for p in parameters]
    print(results)