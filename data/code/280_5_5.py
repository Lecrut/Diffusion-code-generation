def repeat_action(action):
    return [action() for _ in range(10)]

if __name__ == '__main__':
    results = repeat_action(lambda: "Action repeated")
    print(results)