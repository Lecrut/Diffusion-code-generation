def repeat_and_flatten_list(times):
    original_list = [10, 20]
    repeated_list = original_list * times
    return tuple(repeated_list)

if __name__ == '__main__':
    result = repeat_and_flatten_list(7)
    print(result)