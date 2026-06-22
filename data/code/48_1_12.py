numbers = [10, 45, -3, 200, 7, 89, 15, -100, 300, 21]

def find_largest(nums):
    return max([n for n in nums])

if __name__ == '__main__':
    result = find_largest(numbers)
    print(result)