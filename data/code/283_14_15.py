def all_even(numbers):
    return all(x % 2 == 0 for x in numbers)

if __name__ == '__main__':
    sample1 = [2, 4, 6, 8]
    sample2 = [2, 3, 5, 7]
    print(f"All elements in sample1 are even: {all_even(sample1)}")
    print(f"All elements in sample2 are even: {all_even(sample2)}")