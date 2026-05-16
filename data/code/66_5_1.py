def check_adjacent_strictly_increasing(numbers):
    result = []
    for i in range(len(numbers) - 1):
        if numbers[i+1] > numbers[i]:
            result.append(True)
        else:
            result.append(False)
    return result
if __name__ == '__main__':
    sample_list = [1.0, 2.5, 3.0, 1.5, 5.0, 5.0]
    output = check_adjacent_strictly_increasing(sample_list)
    print(output)