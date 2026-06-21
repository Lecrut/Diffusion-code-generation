import statistics

def calculate_mean(numbers):
    if not numbers:
        return None
    try:
        return statistics.mean(numbers)
    except Exception as e:
        print(f"Error calculating mean: {e}")
        return None

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    empty_list = []
    negative_values = [-1, -5, -10]
    
    print(f"Mean of {sample_values}: {calculate_mean(sample_values)}")
    print(f"Mean of {empty_list}: {calculate_mean(empty_list)}")
    print(f"Mean of {negative_values}: {calculate_mean(negative_values)}")