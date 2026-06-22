def repeat_action(times, result_list):
    if times == 0:
        return result_list
    else:
        result_list.append("Action")
        return repeat_action(times - 1, result_list)

if __name__ == '__main__':
    sample_result = repeat_action(10, [])
    print(sample_result)