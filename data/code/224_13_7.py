class ArrayProcessor:
    DEFAULT_ARRAY = [4, 8, 12, 16]
    
    @staticmethod
    def calculate_mean(arr):
        total = sum(arr)
        count = len(arr)
        average = total / count
        return average

if __name__ == '__main__':
    processor = ArrayProcessor()
    mean_value = processor.calculate_mean(ArrayProcessor.DEFAULT_ARRAY)
    print(mean_value)