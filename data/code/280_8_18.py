def repeat_action(times, action, result=None):
    if result is None:
        result = []
    if times == 0:
        return result
    else:
        action()
        result.append(action())
        return repeat_action(times - 1, action, result)

def sample_action():
    return "Action"

if __name__ == '__main__':
    results = repeat_action(10, sample_action)
    print(results)