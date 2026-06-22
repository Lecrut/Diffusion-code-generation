def repeat_action(action, params):
    return [action(param) for param in params]

if __name__ == '__main__':
    def sample_action(x):
        return x * 2

    parameters = [1, 2, 3, 4, 5]
    results = repeat_action(sample_action, parameters)
    print(results)