def repeat_action(message, times):
    for _ in range(times):
        print(message)
if __name__ == '__main__':
    action = 'Repeat an action many times now'
    repetitions = 5
    repeat_action(action, repetitions)