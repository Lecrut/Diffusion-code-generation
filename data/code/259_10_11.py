def find_extremes(data):
    if not data:
        return None
    smallest = min(data)
    largest = max(data)
    return smallest, largest

if __name__ == '__main__':
    sample_list = [42, 15, 89, 3, 77, 5]
    extremes = find_extremes(sample_list)
    print(f"Extremes: {extremes}")