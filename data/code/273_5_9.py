def repeat_action(action, count):
    if count <= 0:
        return
    action()
    repeat_action(action, count - 1)

if __name__ == '__main__':
    def sample_action():
        print("Action repeated")

    repeat_action(sample_action, 3)