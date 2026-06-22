def find_minimum(numbers):
    return min(numbers) if numbers else None

if __name__ == '__main__':
    sample_list = [34, 7, 23, 32, 5, 62]
    print(find_minimum(sample_list))