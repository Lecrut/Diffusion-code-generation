def is_even(number):
    return number % 2 == 0

def count_evens(numbers):
    count = 0
    index = 0
    while index < len(numbers):
        if is_even(numbers[index]):
            count += 1
        index += 1
    return count

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(f"Number of even numbers in {sample_list}: {count_evens(sample_list)}")