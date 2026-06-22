def repeat_action(action, times, result=None):
    if result is None:
        result = []
    if times == 0:
        return result
    else:
        action()
        result.append(action())
        return repeat_action(action, times - 1, result)

if __name__ == '__main__':
    def sample_action():
        return "Action"

    results = repeat_action(sample_action, 10)
    print(results)