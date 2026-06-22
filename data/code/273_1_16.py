def repeat_action(action, N):
    if not isinstance(N, int) or N < 0:
        raise ValueError("N must be a non-negative integer")
    results = []
    i = 0
    while i < N:
        results.append(action())
        i += 1
    return results

if __name__ == '__main__':
    sample_action = lambda: "Action executed"
    result = repeat_action(sample_action, 10)
    print(result)