NUMBERS = [5, 10, 15, 20, 25]

def calculate_average(nums):
    total = sum(nums)
    count = len(nums)
    return total / count

if __name__ == '__main__':
    sample_numbers = NUMBERS
    avg = calculate_average(sample_numbers)
    print(avg)