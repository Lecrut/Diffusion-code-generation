def calculate_mean(scores):
    if not scores:
        return None
    total = sum(scores)
    count = len(scores)
    if count == 0:
        return None
    return total / count

if __name__ == '__main__':
    sample_input = [10, 20, 30, 40]
    mean_value = calculate_mean(sample_input)
    print(f"The mean of {sample_input} is: {mean_value}")
    
    empty_input = []
    mean_value_empty = calculate_mean(empty_input)
    print(f"The mean of an empty list is: {mean_value_empty}")