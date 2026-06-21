def avg(nums):
    return sum(nums) / len(nums) if nums else 0

if __name__ == '__main__':
    print(avg([1, 2, 3]))
    print(avg([]))