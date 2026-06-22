def repeat_action(action, times):
    if times <= 0:
        return
    action()
    repeat_action(action, times - 1)

if __name__ == '__main__':
    def sample_action():
        print("Action executed")

    repeat_action(sample_action, 3)