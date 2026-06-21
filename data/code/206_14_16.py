min_value = lambda lst: min(lst) if lst else None

if __name__ == '__main__':
    sample1 = [3, 1, 4, 1, 5]
    sample2 = [7]
    sample3 = []
    
    def print_min(lst):
        print(f"Minimum in {lst}: {min_value(lst)}")
    
    print_min(sample1)
    print_min(sample2)
    print_min(sample3)