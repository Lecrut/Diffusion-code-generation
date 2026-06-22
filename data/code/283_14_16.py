def all_even(numbers):
    return all(num % 2 == 0 for num in numbers)

if __name__ == '__main__':
    sample1 = [2, 4, 6, 8]
    sample2 = [2, 3, 4, 6]
    print(f"All elements in {sample1} are even: {all_even(sample1)}")
    print(f"All elements in {sample2} are even: {all_even(sample2)}")