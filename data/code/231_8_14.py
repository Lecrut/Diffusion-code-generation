REPEAT_COUNT = 7
LIST_TO_REPEAT = [10, 20]

def repeat_and_flatten(lst, count):
    return tuple(item for sublist in [lst] * count for item in sublist)

if __name__ == '__main__':
    result = repeat_and_flatten(LIST_TO_REPEAT, REPEAT_COUNT)
    print(result)