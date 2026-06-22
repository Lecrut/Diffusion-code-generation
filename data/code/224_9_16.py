class Statistics:
    @staticmethod
    def calculate_mean(numbers):
        if not numbers:
            return 0
        total = sum(numbers)
        count = len(numbers)
        return total / count

if __name__ == '__main__':
    data1 = [10, 20, 30, 40, 50]
    stats_instance = Statistics()
    mean_value = stats_instance.calculate_mean(data1)
    print(f"Mean of {data1}: {mean_value}")