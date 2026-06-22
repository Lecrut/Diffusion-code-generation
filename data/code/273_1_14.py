def repeat_action(action):
    count = 0
    while count < 10:
        try:
            action()
            count += 1
        except TypeError as e:
            print(f"Error: {e}")
            break

if __name__ == '__main__':
    def sample_action():
        print("Action executed")

    repeat_action(sample_action)