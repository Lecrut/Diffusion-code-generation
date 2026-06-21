def compute_average(values):
    if not values:
        return 0
    return sum(values) / len(values)

if __name__ == '__main__':
    sample_list = [5, 10, 15]
    another_list = [-5, 0, 5, 10]
    empty_list = []
    
    avg1 = compute_average(sample_list)
    print(f"The average of {sample_list} is: {avg1}")
    
    avg2 = compute_average(another_list)
    print(f"The average of {another_list} is: {avg2}")
    
    avg3 = compute_average(empty_list)
    print(f"The average of an empty list is: {avg3}")