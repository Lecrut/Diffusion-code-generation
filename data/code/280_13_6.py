MAX_ITERATIONS = 5

def perform_action(param1, param2):
    return f"Action performed with {param1} and {param2}"

if __name__ == '__main__':
    parameters = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]
    results = [perform_action(p[0], p[1]) for p in parameters]
    print(results)