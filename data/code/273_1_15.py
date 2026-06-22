MAX_ITERATIONS = 10

def repeat_action(action):
    for _ in range(MAX_ITERATIONS):
        action()

if __name__ == '__main__':
    def sample_action():
        print("Action executed")

    repeat_action(sample_action)