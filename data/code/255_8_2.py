import sys
def find_maximum(data_string):
    numbers = data_string.split(',')
    if not numbers or (len(numbers) == 1 and not numbers[0].strip()):
        return None
    try:
        nums = [float(n.strip()) for n in numbers if n.strip()]
        if not nums:
            return None
        return max(nums)
    except ValueError:
        return None
if __name__ == '__main__':
    input_data = "10,5,22,8,15"
    result = find_maximum(input_data)
    print(result)