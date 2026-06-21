def calculate_list_sum(iterable):
    total = 0
    for number in iterable:
        total += number
    return total

if __name__ == '__main__':
    sample_lists = {
        'integers': [1, 2, 3, 4, 5],
        'mixed_numbers': [10.5, 20.5, 30.5],
        'mixed_signs': [-1, 5, -10, 2],
        'empty': []
    }
    
    for name, lst in sample_lists.items():
        print(f"Sum of {lst}: {calculate_list_sum(lst)}")