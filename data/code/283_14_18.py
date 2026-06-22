EVEN_NUMBER = 2

def all_even_numbers(input_list):
    return all(x % EVEN_NUMBER == 0 for x in input_list)

if __name__ == '__main__':
    sample_lists = [
        [2, 4, 6, 8],
        [1, 3, 5, 7],
        [],
        [10, 20, 30, 40],
        [11, 22, 33, 44]
    ]
    
    for lst in sample_lists:
        print(f"List {lst} contains all even numbers: {all_even_numbers(lst)}")