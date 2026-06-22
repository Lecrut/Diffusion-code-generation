def repeat_action(action, times):
    if times == 0:
        return
    action()
    repeat_action(action, times - 1)

def sample_action():
    print("Action repeated")

if __name__ == '__main__':
    repeat_action(sample_action, 3)