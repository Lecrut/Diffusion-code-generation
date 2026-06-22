def calculate_difference_of_extremes(d: dict) -> int:
    if not d:
        raise ValueError("Dictionary cannot be empty.")
    return max(d.values()) - min(d.values())

if __name__ == '__main__':
    sample_dict = {
        'apple': 5,
        'banana': 3,
        'cherry': 8
    }
    result = calculate_difference_of_extremes(sample_dict)
    print(f"Difference between the maximum and minimum values in {sample_dict}: {result}")