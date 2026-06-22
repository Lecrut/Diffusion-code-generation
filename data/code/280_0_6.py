def repeat_action(times):
    action_map = {i: f"Iteration {i+1}" for i in range(times)}
    for _ in range(times):
        print(action_map[_])

if __name__ == '__main__':
    repeat_action(10)