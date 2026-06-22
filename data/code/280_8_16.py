def repeat_action(n, result=None):
    if result is None:
        result = []
    if n == 0:
        return result
    else:
        result.append(f"Action {n}")
        return repeat_action(n - 1, result)

if __name__ == '__main__':
    print(repeat_action(10))