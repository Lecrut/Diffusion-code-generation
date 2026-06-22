import random
import time

class MaxValueFinder:
    SAMPLE_SIZES = [10**3, 10**4, 10**5, 10**6]
    
    @staticmethod
    def generate_random_list(size):
        return [random.randint(0, size) for _ in range(size)]
    
    @staticmethod
    def find_max_value(lst):
        max_val = lst[0]
        for num in lst:
            if num > max_val:
                max_val = num
        return max_val
    
    @staticmethod
    def measure_time_taken(func, *args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        return result, end_time - start_time

if __name__ == '__main__':
    for size in MaxValueFinder.SAMPLE_SIZES:
        lst = MaxValueFinder.generate_random_list(size)
        max_value, time_taken = MaxValueFinder.measure_time_taken(MaxValueFinder.find_max_value, lst)
        print(f"List size: {size}, Max value: {max_value}, Time taken: {time_taken:.6f} seconds")