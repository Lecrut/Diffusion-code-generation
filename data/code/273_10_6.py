def perform_sequence():
    print('Hello')
    result = (2 + 3) * 4
    return result

def repeat_three_times(action):
    for _ in range(3):
        action()

if __name__ == '__main__':
    def sample_action():
        greeting, result = perform_sequence()
        print(greeting)
        print(result)

    repeat_three_times(sample_action)