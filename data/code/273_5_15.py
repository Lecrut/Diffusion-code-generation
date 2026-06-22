def repeat_action(action, count=3):
    if count <= 0:
        return
    action()
    repeat_action(action, count - 1)

if __name__ == '__main__':
    def sample_action():
        print("Action executed")

    repeat_action(sample_action)