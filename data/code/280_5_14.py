def repeat_action(action, times):
    return [action() for _ in range(times)]

if __name__ == '__main__':
    def sample_action():
        return "Action Executed"

    result = repeat_action(sample_action, 10)
    print(result)