def repeat_pattern(base_list, target_length):
    if not base_list:
        return []
    
    result = []
    for i in range(target_length):
        result.append(base_list[i % len(base_list)])
    
    return result

if __name__ == '__main__':
    base_list = [1, 2, 3]
    target_length = 7
    result = repeat_pattern(base_list, target_length)
    print(result)