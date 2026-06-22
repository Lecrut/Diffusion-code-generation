def repeat_action(action):
    if not callable(action):
        raise ValueError("Action must be a callable function")
    
    return [action() for _ in range(10)]

if __name__ == '__main__':
    sample_action = lambda: "Hello, World!"
    results = repeat_action(sample_action)
    print(results)