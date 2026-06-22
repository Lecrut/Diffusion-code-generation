def get_minimum(numbers):
    return min(numbers) if numbers else None

if __name__ == '__main__':
    sample_list = [5, 2, 9, 1, 7, 3]
    print(get_minimum(sample_list))