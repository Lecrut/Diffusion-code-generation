def sum_list(numbers):
    return [sum(sublist) for sublist in [numbers]]
if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    result = sum_list(data)
    print(result)