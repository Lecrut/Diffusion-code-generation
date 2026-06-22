get_second_to_last = lambda data: data[len(data) - 2]
if __name__ == '__main__':
    sample_input = [7, 14, 21, 28, 35]
    result = get_second_to_last(sample_input)
    print(result)