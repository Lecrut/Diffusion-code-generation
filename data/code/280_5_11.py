def repeat_action(times=10):
    return [f"Action {i+1}" for i in range(times)]

if __name__ == '__main__':
    result = repeat_action()
    print(result)