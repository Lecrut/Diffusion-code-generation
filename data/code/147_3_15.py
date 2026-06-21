def sort_floats_desc(numbers):
    if all(isinstance(x, float) for x in numbers):
        return sorted(numbers, reverse=True)
    else:
        raise ValueError("All elements must be floats")

if __name__ == '__main__':
    sample_list = [3.5, 1.2, 4.8, 2.9]
    try:
        result = sort_floats_desc(sample_list)
        print(result)
    except Exception as e:
        print(f"Error: {e}")