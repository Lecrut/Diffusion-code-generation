class Statistics:
    @staticmethod
    def compute_mean(numbers):
        if not numbers:
            raise ValueError("The iterable cannot be empty")
        
        total_sum = sum(numbers)
        count = len(numbers)
        
        return total_sum / count

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    average = Statistics.compute_mean(sample_data)
    print(f"Average: {average}")