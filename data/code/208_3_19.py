if __name__ == '__main__':
    SAMPLE_DATA = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    
    def calculate_mean(numbers):
        total_sum = sum(numbers)
        count = len(numbers)
        return total_sum / count if numbers else 0
    
    mean_value = calculate_mean(SAMPLE_DATA)
    print(f"The mean of the sequence is: {mean_value}")