def find_range(numbers):
    if len(numbers) == 0:
        return None
    elif len(numbers) == 1:
        return 0
    else:
        return max(numbers) - min(numbers)
if __name__ == '__main__':
    sample_values = [5, 3, 9, 1, 7]
    print(find_range(sample_values))