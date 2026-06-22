def all_even(numbers):
    return all(num % 2 == 0 for num in numbers)

if __name__ == '__main__':
    sample_lists = [
        [2, 4, 6, 8],
        [1, 3, 5, 7],
        [2, 4, 5, 8],
        [],
        [10]
    ]
    
    for i, lst in enumerate(sample_lists):
        print(f"List {i+1} is all even: {all_even(lst)}")