def repeat_and_flatten(lst, times):
    repeated = [item for sublist in [lst] * times for item in sublist]
    return tuple(repeated)

if __name__ == '__main__':
    sample_list = [10, 20]
    repetitions = 7
    result = repeat_and_flatten(sample_list, repetitions)
    print(result)