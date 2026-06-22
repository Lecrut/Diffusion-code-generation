def repeat_action(times):
    if times < 0:
        raise ValueError("Times must be non-negative")
    if times == 0:
        return []
    else:
        return [f"Action {times}"] + repeat_action(times - 1)

if __name__ == '__main__':
    sample_values = []
    final_result = repeat_action(10)
    print(final_result)