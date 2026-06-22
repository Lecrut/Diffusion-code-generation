REPEAT_COUNT = 10

def repeat_action(times):
    for i in range(times):
        print(f"Iteration {i + 1}")

if __name__ == '__main__':
    repeat_action(REPEAT_COUNT)