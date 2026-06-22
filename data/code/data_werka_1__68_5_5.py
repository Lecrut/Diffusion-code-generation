def absolute_differences_iter(numbers):
    prev = numbers[0] if numbers else None
    for num in numbers:
        if prev is not None:
            yield abs(num - prev)
        prev = num

if __name__ == '__main__':
    sample_list = [7, 1, 9, 3, 6]
    diff_iter = absolute_differences_iter(sample_list)
    result = list(diff_iter)
    print(result)