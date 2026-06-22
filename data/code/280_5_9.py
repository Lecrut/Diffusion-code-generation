MAX_REPETITIONS = 10

def repeat_action(action):
    return [action() for _ in range(MAX_REPETITIONS)]

if __name__ == '__main__':
    result = repeat_action(lambda: 'Action repeated')
    print(result)