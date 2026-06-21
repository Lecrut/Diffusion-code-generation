if __name__ == '__main__':
    sample_tuple = (10, 23, 45, 68, 90, 113)
    
    def extract_odd_numbers(numbers):
        return tuple(x for x in numbers if x % 2 != 0)
    
    odd_numbers = extract_odd_numbers(sample_tuple)
    print(odd_numbers)