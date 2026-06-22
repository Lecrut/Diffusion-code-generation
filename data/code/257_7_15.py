def calculate_difference_of_extremes(d: dict) -> int:
    if not d:
        raise ValueError("Dictionary cannot be empty.")
    return max(d.values()) - min(d.values())

if __name__ == '__main__':
    sample_dict = {
        'apple': 10,
        'banana': 5,
        'cherry': 20
    }
    result = calculate_difference_of_extremes(sample_dict)
    print(f"Difference between max and min values: {result}")