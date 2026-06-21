def find_largest_number(numbers):
    return max(numbers) if numbers else None

if __name__ == '__main__':
    sample_data = [10, 5, 22, 8, 30, 15]
    print(find_largest_number(sample_data))