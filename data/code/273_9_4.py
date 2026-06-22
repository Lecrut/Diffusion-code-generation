def repeat_action(action):
    return [action() for _ in range(5)]

if __name__ == '__main__':
    def sample_action():
        print('Action executed')
    
    results = repeat_action(sample_action)
    for result in results:
        print(result)