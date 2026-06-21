class MeanCalculator:
    @staticmethod
    def calculate_mean(data):
        if not data:
            return None
        
        total = 0
        count = 0
        for value in data:
            total += value
            count += 1
        
        return total / count

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    mean_value = MeanCalculator.calculate_mean(sample_data)
    print(mean_value)
    
    sample_data_2 = [1.5, 2.5, 3.5, 4.5]
    mean_value_2 = MeanCalculator.calculate_mean(sample_data_2)
    print(mean_value_2)