numbers = [3, 5, 8, 10, 23, 45, 60, 70]

def process_numbers(nums):
    for num in nums:
        if num > 50:
            break
        if num % 2 == 0:
            continue
        print(num)

if __name__ == '__main__':
    process_numbers(numbers)