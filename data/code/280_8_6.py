def repeat_action(n, result_list):
    if n == 0:
        return result_list
    else:
        result_list.append(f"Action {n}")
        return repeat_action(n - 1, result_list)

if __name__ == '__main__':
    sample_result = repeat_action(10, [])
    print(sample_result)