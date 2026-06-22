def repeat_action_with_error_handling():
    actions = {
        1: 'move',
        2: 'jump',
        3: 'attack'
    }
    
    for i in range(1, 26):
        try:
            action = actions[i]
            print(f'Action {i}: {action}')
        except KeyError as e:
            print(f'Error: Action {i} not found')

if __name__ == '__main__':
    repeat_action_with_error_handling()