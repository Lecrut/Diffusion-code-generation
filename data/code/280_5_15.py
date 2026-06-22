def repeat_action(times):
    return [f"Action {i+1}" for i in range(times)]

if __name__ == '__main__':
    result = repeat_action(10)
    print(result)