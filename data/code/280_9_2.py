def repeat_list_actions(actions, n):
    result = []
    for action in actions:
        result.extend([action] * n)
    return result
if __name__ == '__main__':
    sample_actions = ["move", "jump", "say"]
    repetition_factor = 3
    repeated_actions = repeat_list_actions(sample_actions, repetition_factor)
    print(repeated_actions)