def perform_action(param):
    return param * 2

if __name__ == '__main__':
    params = [1, 2, 3, 4, 5]
    results = [perform_action(p) for p in params]
    print(results)