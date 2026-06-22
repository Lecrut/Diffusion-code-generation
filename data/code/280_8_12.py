def repeat_action(n, result=None):
    if n == 0:
        return result or []
    else:
        action_result = f"Action {n}"
        if result is None:
            result = [action_result]
        else:
            result.append(action_result)
        return repeat_action(n - 1, result)

if __name__ == '__main__':
    results = repeat_action(10)
    print(results)