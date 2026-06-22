def repeat_and_flatten(lst, times):
    return tuple(item for sublist in [lst] * times for item in sublist)

if __name__ == '__main__':
    result = repeat_and_flatten([10, 20], 7)
    print(result)