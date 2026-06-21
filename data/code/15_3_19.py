def get_second_last(numbers):
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")
    return numbers[-2]

if __name__ == '__main__':
    sample_data = [10, 25, 30, 45, 50]
    result = get_second_last(sample_data)
    print(result)