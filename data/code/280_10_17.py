def repeat_action(action, count):
    for _ in range(count):
        action()

def print_message():
    print('Repeat an action many times now')

if __name__ == '__main__':
    action_to_repeat = print_message
    count_to_repeat = 5
    repeat_action(action_to_repeat, count_to_repeat)