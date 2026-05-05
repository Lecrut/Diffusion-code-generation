def check_adjacent_increase(numbers):
    result = []
    for i in range(len(numbers) - 1):
        if numbers[i+1] > numbers[i]:
            result.append(True)
        else:
            result.append(False)
    return result
if __name__ == '__main__':
    sample_list = [1.0, 2.5, 3.0, 1.5, 4.0]
    output = check_adjacent_increase(sample_list)
    print(output)