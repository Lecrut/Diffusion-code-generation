def average(nums):
    return sum(nums) / len(nums) if nums else 0

if __name__ == '__main__':
    print(average([1, 2, 3, 4, 5]))
    print(average([]))