def find_maximum(numbers):
    if not numbers:
        return None
    maximum = numbers[0]
    for i in range(1, len(numbers)):
        current_value = numbers[i]
        if current_value > maximum:
            maximum = current_value
    return maximum
if __name__ == '__main__':
    sample_list = [34, 78, 25, 90, -10, 67]
    result = find_maximum(sample_list)
    print(result)