def repeat_action(action, times):
    return [action() for _ in range(times)]

if __name__ == '__main__':
    sample_action = lambda: "Action Repeated"
    repeated_actions = repeat_action(sample_action, 10)
    print(repeated_actions)