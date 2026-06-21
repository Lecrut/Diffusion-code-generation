def get_third_item(numbers):
    if len(numbers) < 3:
        return None
    return numbers[2]

if __name__ == '__main__':
    sample_array = [10, 20, 30, 40, 50]
    result = get_third_item(sample_array)
    print(result)