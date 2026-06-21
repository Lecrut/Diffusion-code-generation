def calculate_mean(data):
    if not all(isinstance(item, (int, float)) for item in data):
        raise ValueError("List contains non-numeric types")
    return sum(data) / len(data)

if __name__ == '__main__':
    sample_list = [5, 10, 15, 20, 25]
    try:
        print(f"Mean of {sample_list}: {calculate_mean(sample_list)}")
    except ValueError as e:
        print(e)