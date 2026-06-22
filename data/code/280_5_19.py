def repeat_action_ten_times(action):
    return [action() for _ in range(10)]

if __name__ == '__main__':
    def sample_action():
        return "Action repeated"

    repeated_actions = repeat_action_ten_times(sample_action)
    print(repeated_actions)