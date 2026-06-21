from functools import reduce

average = lambda nums: reduce(lambda x, y: x + y, nums) / len(nums) if nums else 0

if __name__ == '__main__':
    sample_values = [1.5, 2.5, 3.5]
    print(average(sample_values))