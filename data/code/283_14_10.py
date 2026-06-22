def all_even_numbers(input_list):
    return all(x % 2 == 0 for x in input_list)

if __name__ == '__main__':
    sample1 = [2, 4, 6, 8]
    sample2 = [1, 3, 5, 7]
    sample3 = [2, 3, 6, 8]
    
    print(f"All numbers in {sample1} are even: {all_even_numbers(sample1)}")
    print(f"All numbers in {sample2} are even: {all_even_numbers(sample2)}")
    print(f"All numbers in {sample3} are even: {all_even_numbers(sample3)}")