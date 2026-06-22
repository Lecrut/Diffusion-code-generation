def repeat_action(action):
    return [action() for _ in range(10)]

if __name__ == '__main__':
    def sample_action():
        return "Action"

    results = repeat_action(sample_action)
    print(results)