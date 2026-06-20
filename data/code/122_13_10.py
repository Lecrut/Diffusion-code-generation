NUMBERS = [3.5, 2.1, 4.8, 6.7]

def calculate_mean(nums):
    return sum(nums) / len(nums)

if __name__ == '__main__':
    print(calculate_mean(NUMBERS))