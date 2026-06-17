def repeat_iterable(iterable, n):
    if n <= 0:
        return
    current_list = []
    for _ in range(n):
        current_list.extend(iterable)
    for item in current_list:
        yield item
if __name__ == '__main__':
    my_list = [1, 2]
    repetitions = 3
    result_generator = repeat_iterable(my_list, repetitions)
    output = list(result_generator)
    print(output)