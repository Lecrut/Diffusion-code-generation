min_value = lambda lst: min(lst) if lst else None

if __name__ == '__main__':
    sample_data = [5, 3, 9, 1, 0]
    result = min_value(sample_data)
    print(f"Minimum in {sample_data}: {result}")