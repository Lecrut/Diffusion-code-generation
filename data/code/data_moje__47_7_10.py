def find_mean(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1
    return total / count

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(find_mean(sample_list))