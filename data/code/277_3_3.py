def count_elements(iterable):
    count = 0
    iterator = iter(iterable)
    while True:
        try:
            next(iterator)
            count += 1
        except StopIteration:
            break
    return count
if __name__ == '__main__':
    sample_string = "hello"
    sample_list = [1, 2, 3, 4, 5]
    result_string = count_elements(sample_string)
    print(f"The number of characters in '{sample_string}' is: {result_string}")
    result_list = count_elements(sample_list)
    print(f"The number of elements in {sample_list} is: {result_list}")