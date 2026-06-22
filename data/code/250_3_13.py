NUMBERS = [10, 20, 30, 40]

def calculate_average(nums):
    return sum(nums) / len(nums)

if __name__ == '__main__':
    avg = calculate_average(NUMBERS)
    print(avg)