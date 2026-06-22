import math

def get_median(elements):
    if not elements:
        raise ValueError("List must not be empty")
    
    n = len(elements)
    sorted_elems = sorted(elements)
    
    if n % 2 == 1:
        mid_index = n // 2
        return sorted_elems[mid_index]
    else:
        mid_index_1 = (n // 2) - 1
        mid_index_2 = n // 2
        mid_val_1 = sorted_elems[mid_index_1]
        mid_val_2 = sorted_elems[mid_index_2]
        return (mid_val_1 + mid_val_2) / 2.0

if __name__ == '__main__':
    sample_data = [12, 4, 5, 3, 7, 19, 1, 10]
    median_value = get_median(sample_data)
    print(median_value)